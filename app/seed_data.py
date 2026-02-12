from sqlmodel import Session, create_engine
from app.models import Vessel, Alert, Geofence
from app.config import settings
from loguru import logger

# CONF23-STD-SDLC-NAVMIL: Standardized Seed Data

engine = create_engine(settings.DATABASE_URL)

def generate_sample_data():
    """Populates the local database with consistent maritime intelligence data."""
    logger.info("Generating coherent sample data for NAVINT...")
    
    with Session(engine) as session:
        # 1. Standardized Vessels
        v1 = Vessel(mmsi=224123456, name="VIVA ESPANA", flag="ES", vessel_type="Cargo", risk_score=0.15)
        v2 = Vessel(mmsi=351987654, name="OCEAN MARAUDER", flag="PA", vessel_type="Tanker", risk_score=settings.RISK_THRESHOLD_HIGH + 0.05)
        v3 = Vessel(mmsi=667001122, name="DARK STAR", flag="SL", vessel_type="Tug", risk_score=0.95)
        
        session.add(v1)
        session.add(v2)
        session.add(v3)
        
        # 2. Strategic Geofence (Polygon bounding box)
        g1 = Geofence(
            name="Strategic Asset Alpha", 
            geometry_json='{"type":"Polygon","coordinates":[[[-6.35,36.55],[-6.15,36.55],[-6.15,36.35],[-6.35,36.35],[-6.35,36.55]]]}', 
            risk_level="CRITICAL"
        )
        session.add(g1)
        
        session.commit()
        logger.info("Sample data coherence verified and inserted.")

if __name__ == "__main__":
    generate_sample_data()
