from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

# CONF23-STD-SDLC-NAVMIL: API Schemas (Pydantic v2)

class VesselBase(BaseModel):
    mmsi: int
    imo: Optional[int] = None
    name: str
    flag: str
    vessel_type: str

class VesselRead(VesselBase):
    id: int
    risk_score: float
    last_seen: datetime

    class Config:
        from_attributes = True

class GeofenceBase(BaseModel):
    name: str
    geometry_json: str
    risk_level: str

class GeofenceRead(GeofenceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class AlertRead(BaseModel):
    id: int
    vessel_mmsi: int
    alert_type: str
    severity: str
    message: str
    timestamp: datetime
    acknowledged: bool

    class Config:
        from_attributes = True
