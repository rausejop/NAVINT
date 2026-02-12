from sqlmodel import Session, create_engine
from app.models import Vessel, Alert, Geofence
from datetime import datetime
from loguru import logger

# CONF23-STD-SDLC-NAVMIL: Sample Data Generator
# Strictly for demonstration purposes in the local environment

sqlite_url = "sqlite:///data/navint.db"
engine = create_engine(sqlite_url)

def generate_sample_data():
    """Populates the local database with sample maritime intelligence data."""
    logger.info("Generating sample data for NAVINT...")
    
    with Session(engine) as session:
        # 1. Sample Vessels
        v1 = Vessel(mmsi=224123456, name="VIVA ESPANA", flag="ES", vessel_type="Cargo", risk_score=0.15)
        v2 = Vessel(mmsi=351987654, name="OCEAN MARAUDER", flag="PA", vessel_type="Tanker", risk_score=0.85)
        v3 = Vessel(mmsi=667001122, name="DARK STAR", flag="SL", vessel_type="Pleasure Craft", risk_score=0.95)
        
        session.add(v1)
        session.add(v2)
        session.add(v3)
        
        # 2. Sample Geofence
        g1 = Geofence(name="Strategic Asset Alpha", geometry_json='{"type":"Polygon","coordinates":[[[-6.3,36.5],[-6.2,36.5],[-6.2,36.4],[-6.3,36.4],[-6.3,36.5]]]}', risk_level="CRITICAL")
        session.add(g1)
        
        # 3. Sample Alert
        a1 = Alert(vessel_mmsi=667001122, alert_type="GEOPROXIMITY", severity="CRITICAL", message="Vessel DARK STAR entered a restricted strategic zone.")
        session.add(a1)
        
        session.commit()
        logger.info("Sample data inserted successfully.")

if __name__ == "__main__":
    generate_sample_data()
