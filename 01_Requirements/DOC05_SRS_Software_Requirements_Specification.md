# DOC05 - SRS: Software Requirements Specification
## NAVINT - Maritime Intelligence Predictive Platform

**Document Version:** 1.2  
**Date:** 2026-02-12  
**Classification:** USO OFICIAL  
**Project Category:** WEB (Local Standalone)
**License:** Apache License 2.0

---

## 1. SOFTWARE STACK
- **Backend**: FastAPI (Python 3.14.2).
- **Frontend**: Next.js (React).
- **Database**: SQLite (SQLModel).
- **Logging**: `loguru` (Structured JSON).

---

## 2. COMPONENT DECOMPOSITION

### 2.1 Unified Next.js Frontend
- **Operational Dashboard**: Map-centric view for real-time tracking.
- **Intelligence Module**: Pane for vessel deep-dives and corporate intelligence.
- **Analytics Panel**: Integrated charts and risk scoring controls.
- **State Management**: React Context or Zustand for keeping vessel positions synced across the UI.

### 2.2 FastAPI Intelligence Service
- **AIS Handler**: Async ingestion from local streams.
- **Risk Core**: Python 3.14 logic with `asyncio` loop for anomaly checks.
- **API v1**: REST endpoints serving the Next.js frontend.
- **WS Server**: Pushing real-time vessels to the client.

### 2.3 Persistence (SQLite)
- Tables: `Vessels`, `History`, `Geofences`, `AuditLogs`, `Companies`.

---

## 3. INTERFACES
- **Internal**: REST + WebSockets over `localhost`.
- **External**: AIS NMEA stream ingestion.

---

**Document Control:**
- **Version:** 1.2 (Unified Next.js edition)
- **Status:** Final Software Spec
- **Classification:** USO OFICIAL
