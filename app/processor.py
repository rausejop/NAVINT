import asyncio
import json
from sqlmodel import Session, select, create_engine
from loguru import logger

from app.models import Vessel, Alert, Geofence
from app.risk_engine import RiskEngine
from app.config import settings
from app.websocket_manager import socket_manager

# CONF23-STD-SDLC-NAVMIL: Integrated Message Processor
# Standardizing logic flow and dependency management

engine = create_engine(settings.DATABASE_URL)

class GeofenceManager:
    """Handles spatial proximity checks between vessels and geofences."""
    @staticmethod
    def is_inside(lat: float, lon: float, geometry_json: str) -> bool:
        try:
            geom = json.loads(geometry_json)
            coords = geom['coordinates'][0]
            lats = [c[1] for c in coords]
            lons = [c[0] for c in coords]
            return (min(lats) <= lat <= max(lats)) and (min(lons) <= lon <= max(lons))
        except Exception as e:
            logger.error(f"Geofence spatial parse error: {e}")
            return False

async def process_ais_message(data: dict):
    """
    Unified processing pipeline:
    State Update -> Spatial Check -> Risk Analysis -> Alerting -> Broadcasting
    """
    with Session(engine) as session:
        # 1. State Persistence
        statement = select(Vessel).where(Vessel.mmsi == data["mmsi"])
        vessel = session.exec(statement).first()
        
        if not vessel:
            vessel = Vessel(
                mmsi=data["mmsi"],
                name=f"Vessel_{data['mmsi']}",
                flag="UNKNOWN",
                last_seen=data["timestamp"]
            )
            session.add(vessel)
        
        vessel.last_seen = data["timestamp"]
        
        # 2. Strategic Geofencing
        geofences = session.exec(select(Geofence)).all()
        near_asset = False
        active_geofence = None
        
        for gf in geofences:
            if GeofenceManager.is_inside(data["lat"], data["lon"], gf.geometry_json):
                near_asset = True
                active_geofence = gf
                break
        
        # 3. Autonomous Risk Scoring
        risk_context = {
            "near_asset": near_asset,
            "anomaly_detected": data.get("anomaly", False)
        }
        vessel.risk_score = await RiskEngine.calculate_score(vessel, risk_context)
        
        # 4. Intelligence Alert Generation
        alert_payload = None
        if near_asset and active_geofence:
            alert = Alert(
                vessel_mmsi=vessel.mmsi,
                alert_type="GEOFENCE_BREACH",
                severity=active_geofence.risk_level,
                message=f"Vessel {vessel.name} breached {active_geofence.name}."
            )
            session.add(alert)
            session.flush()
            alert_payload = {
                "id": alert.id,
                "severity": alert.severity,
                "message": alert.message,
                "timestamp": alert.timestamp.isoformat()
            }

        session.commit()

        # 5. Real-time Broadcasting via Unified Socket Manager
        broadcast_data = {
            "type": "vessel_update",
            "data": {
                "mmsi": vessel.mmsi,
                "name": vessel.name,
                "vessel_type": vessel.vessel_type,
                "lat": data["lat"],
                "lon": data["lon"],
                "risk_score": vessel.risk_score,
                "last_seen": vessel.last_seen.isoformat()
            }
        }
        if alert_payload:
            broadcast_data["alert"] = alert_payload

        # Execute broadcast in a safe background task
        asyncio.create_task(socket_manager.broadcast(json.dumps(broadcast_data)))
