import sys
from typing import List
from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select, create_engine
from loguru import logger
import csv
import os

from app.models import Vessel, Alert
from app.schemas import VesselRead, AlertRead
from app.config import settings
from app.websocket_manager import socket_manager

# CONF23-STD-SDLC-NAVMIL: Enhanced Backend Coherence
# Unified metadata and shared state management

logger.remove()
logger.add(sys.stderr, level="DEBUG", format="{time} {level} {message}")
logger.add(settings.LOG_FILE_PATH, rotation="500 MB", level="DEBUG", serialize=True)

engine = create_engine(settings.DATABASE_URL)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Unified Maritime Intelligence Support Tool (Local Edition)",
    version=settings.PROJECT_VERSION
)

# Shared CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_session():
    with Session(engine) as session:
        yield session

@app.websocket("/ws/vessels")
async def websocket_endpoint(websocket: WebSocket):
    await socket_manager.connect(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        socket_manager.disconnect(websocket)

@app.get("/", tags=["Health"])
async def health_check():
    return {
        "status": "operational", 
        "project": settings.PROJECT_NAME, 
        "version": settings.PROJECT_VERSION
    }

@app.get("/api/v1/vessels", response_model=List[VesselRead], tags=["Intelligence"])
async def get_vessels(session: Session = Depends(get_session)):
    return session.exec(select(Vessel)).all()

@app.get("/api/v1/alerts", response_model=List[AlertRead], tags=["Intelligence"])
async def get_alerts(session: Session = Depends(get_session)):
    return session.exec(select(Alert).order_by(Alert.timestamp.desc())).all()

@app.get("/api/v1/export/vessels", tags=["Reporting"])
async def export_vessels(session: Session = Depends(get_session)):
    """Standardized CSV Export Logic."""
    os.makedirs("exports", exist_ok=True)
    file_path = "exports/vessels_export.csv"
    vessels = session.exec(select(Vessel)).all()
    
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["MMSI", "Name", "Flag", "Type", "Risk Score", "Last Seen"])
        for v in vessels:
            writer.writerow([v.mmsi, v.name, v.flag, v.vessel_type, v.risk_score, v.last_seen])
    
    return FileResponse(file_path, media_type="text/csv", filename="vessels_export.csv")
