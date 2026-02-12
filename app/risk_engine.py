from typing import Dict, Any
from app.models import Vessel
from loguru import logger

# CONF23-STD-SDLC-NAVMIL: Risk Assessment Engine
# Based on multi-factor weighted scoring

class RiskEngine:
    """
    Calculates threat scores for vessels based on behavioral 
    and static indicators.
    """
    
    # Weight configuration
    WEIGHTS = {
        "flag_risk": 0.20,      # Suspicious flag states
        "behavior_risk": 0.40,  # Speed jumps, dark periods
        "proximity_risk": 0.40  # Near critical infrastructure
    }

    @staticmethod
    async def calculate_score(vessel: Vessel, context_data: Dict[str, Any]) -> float:
        """
        Computes a normalized risk score (0.0 to 1.0).
        """
        score = 0.0
        
        # 1. Flag Risk (Example: SL - Sierra Leone or PA - Panama)
        if vessel.flag in ["SL", "KH", "TZ"]:
            score += 1.0 * RiskEngine.WEIGHTS["flag_risk"]
            
        # 2. Behavioral Risk (identity manipulation or signal gaps)
        if context_data.get("anomaly_detected", False):
            score += 1.0 * RiskEngine.WEIGHTS["behavior_risk"]
            
        # 3. Proximity Risk (near strategic assets)
        if context_data.get("near_asset", False):
            score += 1.0 * RiskEngine.WEIGHTS["proximity_risk"]
            
        logger.debug("Calculated risk score for {}: {}", vessel.name, round(score, 2))
        return min(round(score, 2), 1.0)

if __name__ == "__main__":
    # Test stub
    import asyncio
    v = Vessel(name="DARK STAR", flag="SL")
    ctx = {"anomaly_detected": True, "near_asset": True}
    print(asyncio.run(RiskEngine.calculate_score(v, ctx)))
