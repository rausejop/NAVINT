# DOC03 - StRS: Stakeholder Requirements Specification
## NAVINT - Maritime Intelligence Predictive Platform

**Document Version:** 1.2  
**Date:** 2026-02-12  
**Classification:** USO OFICIAL  
**Project Category:** WEB (Local Standalone)
**License:** Apache License 2.0

---

## 1. INTRODUCTION
Documentation of user and stakeholder needs for a unified, standalone maritime intelligence interface.

---

## 2. STAKEHOLDER IDENTIFICATION
- **Intelligence Analysts:** Primary users requiring mapping, search, and risk analysis in one place.
- **Supervisors:** Need audit logs and report exports.
- **System Admins:** Manage the local `build.cmd` and SQLite database.

---

## 3. USER REQUIREMENTS

### 3.1 Unified Interface Perspective
- **UR-01: Consolidated Workspace:** "I want to see the map, the vessel list, and the risk details without switching between different web applications."
- **UR-02: Premium Map Experience:** "I need a smooth, high-performance map in the Next.js interface that can handle hundreds of local targets."
- **UR-03: Real-time Analytics:** "Risk score updates should appear on the main dashboard instantly via WebSockets."

### 3.2 Reporting & Management
- **UR-04: Integrated Search:** "A global search bar that finds vessels, companies, or alerts within the main UI."
- **UR-05: Local Data Export:** "Button to export the current view or specific vessel reports to the local disk."

---

## 4. SYSTEM OPERATIONAL CONCEPT (OpsCon)
The system operates as a **unified local workspace**:
1.  **Backend (API)**: FastAPI manages data and logic.
2.  **Frontend (UI)**: A single Next.js (React) application provides the complete feature set (Monitoring, Analytics, Admin).

---

## 5. UI/UX REQUIREMENTS
- **Performance:** Navigation between 'Map View' and 'Analytical View' within Next.js must be sub-second.
- **Consistency:** Use a single Design System throughout the platform.
- **Aesthetics:** High-fidelity animations and responsive dark-mode layout.

---

**Document Control:**
- **Version:** 1.2 (Unified Next.js edition)
- **Status:** Approved
- **Classification:** USO OFICIAL
