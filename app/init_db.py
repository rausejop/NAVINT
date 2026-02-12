from sqlmodel import SQLModel, create_engine
from app.models import Vessel, Geofence, Alert, AuditLog
from app.config import settings
from loguru import logger
import os

# CONF23-STD-SDLC-NAVMIL: Standardized DB Initialization

def init_db():
    """Initializes the SQLite database within the defined data directory."""
    logger.info(f"Initializing database at {settings.DATABASE_URL}")
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    engine = create_engine(settings.DATABASE_URL)
    SQLModel.metadata.create_all(engine)
    logger.info("Database schema synchronized successfully.")

if __name__ == "__main__":
    init_db()
