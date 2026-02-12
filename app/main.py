import sys
from fastapi import FastAPI, Depends, HTTPException, status
from loguru import logger
import json

from sqlmodel import Session, select, create_engine
from fastapi.middleware.cors import CORSMiddleware
from app.models import Vessel, Alert, Geofence, AuditLog
from app.schemas import VesselRead, AlertRead, GeofenceRead

# CONF23-STD-SDLC-NAVMIL: Structured JSON Logging
logger.remove()
logger.add(sys.stderr, level="DEBUG", format="{time} {level} {message}")
logger.add("logs/navint_{time}.log", rotation="500 MB", level="DEBUG", serialize=True)

sqlite_url = "sqlite:///data/navint.db"
engine = create_engine(sqlite_url)

app = FastAPI(
    title="NAVINT Unified Maritime Intelligence API",
    description="Backend service for standalone Next.js maritime analytics workspace",
    version="1.1.0"
)

# CORS Configuration for localhost development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_session():
    with Session(engine) as session:
        yield session

@app.on_event("startup")
async def startup_event():
    logger.info("NAVINT Backend Service starting...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("NAVINT Backend Service shutting down...")

@app.get("/", tags=["Health"])
async def health_check():
    """Basic health check endpoint."""
    logger.debug("Health check requested")
    return {"status": "operational", "version": "1.0.0"}

@app.get("/api/v1/vessels", response_model=List[VesselRead], tags=["Intelligence"])
async def get_vessels(session: Session = Depends(get_session)):
    """Retrieve list of tracked vessels from the local database."""
    logger.info("Retrieving vessel list")
    vessels = session.exec(select(Vessel)).all()
    return vessels

@app.get("/api/v1/alerts", response_model=List[AlertRead], tags=["Intelligence"])
async def get_alerts(session: Session = Depends(get_session)):
    """Retrieve recent alerts."""
    logger.info("Retrieving alert list")
    alerts = session.exec(select(Alert).order_by(Alert.timestamp.desc())).all()
    return alerts

@app.get("/api/v1/geofences", response_model=List[GeofenceRead], tags=["Configuration"])
async def get_geofences(session: Session = Depends(get_session)):
    """Retrieve all strategic geofences."""
    logger.info("Retrieving geofences")
    geofences = session.exec(select(Geofence)).all()
    return geofences


