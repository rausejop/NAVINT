# DOC01 - CONOPS: Concept of Operations
## NAVINT - Maritime Intelligence Support Tool (Local Edition)

**Document Version:** 1.2  
**Date:** 2026-02-12  
**Classification:** USO OFICIAL  
**Project Category:** WEB / TOOL  
**License:** Apache License 2.0

---

## 1. EXECUTIVE SUMMARY

The NAVINT project provides a standalone maritime intelligence predictive platform for the Maritime Space Monitoring Cell (EMR). This local edition is designed for execution within a controlled localhost environment using a unified modern web interface.

### 1.1 Mission Statement
Enable real-time and predictive maritime intelligence capabilities through automated vessel tracking, risk assessment, and anomaly detection in maritime spaces of strategic interest.

### 1.2 Strategic Context
- **Operational Authority:** Strategic Defense Command
- **End User:** Intelligence Monitoring Unit
- **Deployment Model:** Standalone Web Application (Localhost)
- **Database:** SQLite (Local Persistence)
- **Tech Stack:** Python 3.14.2, FastAPI, Next.js (Unified Frontend)

---

## 2. OPERATIONAL ENVIRONMENT

### 2.1 Current State
The intelligence unit requires enhanced maritime domain awareness capabilities to monitor vessel movements, identify security threats, and analyze corporate relationships within a single, high-performance interface.

### 2.2 Deployment Context
- **Hosting:** Standalone execution on dedicated local workstations.
- **Access:** Local web interface via `localhost` (Next.js).
- **User Base:** Authorized local analysts and supervisors.
- **Data Sensitivity:** Internal/Official Use.

---

## 3. OPERATIONAL CONCEPT

### 3.1 Core Capabilities

#### 3.1.1 Unified Monitoring & Tracking
- Real-time AIS visualization on advanced interactive maps.
- Historical track analysis integrated into the main dashboard.
- Automated zone-based alerting.

#### 3.1.2 Integrated Intelligence Analysis
- Unified view for vessel data and corporate ownership.
- Pattern recognition for risk behaviors.
- Relationship mapping (vessels to corporate entities) in the same operational workspace.

---

## 4. OPERATIONAL SCENARIOS

### 4.1 Scenario: Routine Surveillance
1. Analyst launches the local NAVINT service via `build.cmd`.
2. System initializes the Next.js frontend and FastAPI backend.
3. Analyst monitors the unified dashboard for real-time AIS updates and risk alerts.

### 4.2 Scenario: Investigative Deep-Dive
1. Analyst identifies a suspicious vessel on the map.
2. Analyst clicks the vessel to expand a detailed intelligence panel within the Next.js UI.
3. System correlates local SQLite data to show ownership and risk history instantly.

---

## 5. SYSTEM BOUNDARIES

**In Scope:**
- Unified Web Application (Next.js).
- Backend Business Logic (FastAPI/Python 3.14.2).
- Local Data Storage (SQLite).
- Support for AIS NMEA ingestion.

**Out of Scope:**
- External Multi-tenant Cloud Infrastructure.
- Dedicated Analytics Dashboard (consolidated into primary UI).

---

## 6. OPERATIONAL CONSTRAINTS
- **Performance:** Single UI must manage both mapping and complex data analysis without exceeding memory limits.
- **Security:** Logic and data must remain within the host environment.

---

**Document Control:**
- **Version:** 1.2 (Unified Next.js edition)
- **Status:** Approved
- **Classification:** USO OFICIAL
