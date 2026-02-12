import os
from pydantic_settings import BaseSettings

# CONF23-STD-SDLC-NAVMIL: Centralized Configuration
# Standardizing settings across all backend components

class Settings(BaseSettings):
    PROJECT_NAME: str = "NAVINT Unified Maritime Intelligence"
    PROJECT_VERSION: str = "1.2.0"
    
    # Database
    DATABASE_URL: str = "sqlite:///data/navint.db"
    
    # Networking
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    
    # Application Logic
    AIS_INGESTION_INTERVAL: int = 10
    RISK_THRESHOLD_HIGH: float = 0.8
    
    # Audit & Logs
    LOG_FILE_PATH: str = "logs/navint.log"

    class Config:
        env_file = ".env"

settings = Settings()
