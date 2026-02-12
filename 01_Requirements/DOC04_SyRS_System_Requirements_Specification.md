# DOC04 - SyRS: System Requirements Specification
## NAVINT - Maritime Intelligence Predictive Platform

**Document Version:** 1.2  
**Date:** 2026-02-12  
**Classification:** USO OFICIAL  
**Project Category:** WEB (Local Standalone)
**License:** Apache License 2.0

---

## 1. FUNCTIONAL REQUIREMENTS

### 1.1 Backend System (Python 3.14.2 / FastAPI)
- **SYS-FUNC-001:** Asynchronous AIS data ingestion and SQLite persistence.
- **SYS-FUNC-002:** Implementation of automated risk scoring and anomaly detection models.
- **SYS-FUNC-003:** WebSocket server for real-time state broadcast to the unified UI.

### 1.2 Unified UI (Next.js)
- **SYS-FUNC-004:** Interactive Map Component (Leaflet/Mapbox) for tracking.
- **SYS-FUNC-005:** Integrated Analytics Module for risk parameter tuning and bulk data view.
- **SYS-FUNC-006:** Search and Investigation panel for corporate relationships.
- **SYS-FUNC-007:** Local export engine (PDF/CSV/KML).

---

## 2. NON-FUNCTIONAL REQUIREMENTS

### 2.1 Performance & Resource Management
- **RAM Overhead:** Unified application must maintain < 8GB overhead for the entire suite.
- **UI Responsiveness:** Map rendering > 30 FPS in Next.js on standard hardware.

### 2.2 Security (OWASP Hardening)
- **Hardening:** Mitigation of Web and LLM Top 10 risks within the Next.js/FastAPI stack.
- **Access Control:** Restricted to `localhost` with local token-based sessions.

---

## 3. SYSTEM INTERFACES
- **API Architecture:** RESTful and WebSocket connections between Next.js and FastAPI.
- **Storage:** Local SQLite database file management.

---

**Document Control:**
- **Version:** 1.2 (Unified Next.js edition)
- **Status:** Approved
- **Classification:** USO OFICIAL
