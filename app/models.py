from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

# CONF23-STD-SDLC-NAVMIL: Data Models for SQLite
# Optimized for performance and readability

class Vessel(SQLModel, table=True):
    """Vessel master data."""
    id: Optional[int] = Field(default=None, primary_key=True)
    mmsi: int = Field(index=True, unique=True)
    imo: Optional[int] = Field(default=None, index=True)
    name: str = Field(index=True)
    flag: str
    vessel_type: str
    risk_score: float = Field(default=0.0)
    last_seen: datetime = Field(default_factory=datetime.utcnow)

class Geofence(SQLModel, table=True):
    """User-defined geographic zones."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    geometry_json: str  # Storing as JSON string for SQLite simplicity (WKT or GeoJSON)
    risk_level: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Alert(SQLModel, table=True):
    """Automated intelligence alerts."""
    id: Optional[int] = Field(default=None, primary_key=True)
    vessel_mmsi: int = Field(index=True)
    alert_type: str
    severity: str
    message: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    acknowledged: bool = Field(default=False)

class AuditLog(SQLModel, table=True):
    """Immutable local audit trail."""
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    action: str
    details: str
    user_id: str = Field(default="local_analyst")
