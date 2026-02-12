from typing import List
from fastapi import WebSocket
from loguru import logger

# CONF23-STD-SDLC-NAVMIL: Decoupled WebSocket Manager
# Prevents circular imports and ensures state coherence

class ConnectionManager:
    """
    Manages active WebSocket connections and broadcasts real-time
    updates to all connected local clients.
    """
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"WebSocket Client Connected. Active: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            logger.info(f"WebSocket Client Disconnected. Active: {len(self.active_connections)}")

    async def broadcast(self, message: str):
        """Send message to all active local connections."""
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"Failed to broadcast to connection: {e}")
                # Potentially remove stale connection here

# Singleton instance for the application
socket_manager = ConnectionManager()
