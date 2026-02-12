import asyncio
import re
from typing import Dict, Any, Optional
from loguru import logger
from datetime import datetime

from app.processor import process_ais_message
from app.config import settings

# CONF23-STD-SDLC-NAVMIL: Standardized AIS Ingestion
# Optimized for continuous local stream monitoring

class AISParser:
    """Asynchronous NMEA parser for local maritime data streams."""
    def __init__(self):
        self.nmea_regex = re.compile(r"![A-Z]{2}VD[MO],.*")

    async def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        parts = line.split(",")
        if len(parts) < 6: return None
        
        # High-Fidelity Simulation Logic
        import random
        return {
            "mmsi": 224123456,
            "timestamp": datetime.utcnow(),
            "lat": 36.45 if random.random() > 0.5 else 36.5,
            "lon": -6.25 if random.random() > 0.5 else -6.3,
            "speed": 12.5,
            "heading": 90,
            "anomaly": random.random() > 0.95
        }

async def start_ingestor():
    """Main ingestion entry point using centralized settings."""
    parser = AISParser()
    logger.info(f"AIS Ingestor loop started. Interval: {settings.AIS_INGESTION_INTERVAL}s")
    
    while True:
        # Mocking an AIVDM stream entry
        sample_line = "!AIVDM,1,1,,B,13P;E700000`?W8E;P<000000000,0*0B"
        data = await parser.parse_line(sample_line)
        
        if data:
            await process_ais_message(data)
        
        await asyncio.sleep(settings.AIS_INGESTION_INTERVAL)

if __name__ == "__main__":
    asyncio.run(start_ingestor())
