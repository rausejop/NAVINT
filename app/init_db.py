from sqlmodel import SQLModel, create_engine
from app.models import Vessel, Geofence, Alert, AuditLog
from loguru import logger
import os

# CONF23-STD-SDLC-NAVMIL: Database Initialization
sqlite_url = "sqlite:///data/navint.db"
engine = create_engine(sqlite_url, echo=False)

def init_db():
    """Initializes the SQLite database with the defined schema."""
    logger.info("Initializing database at {}", sqlite_url)
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("Database schema created successfully.")
    except Exception as e:
        logger.error("Failed to initialize database: {}", str(e))
        raise

if __name__ == "__main__":
    init_db()
