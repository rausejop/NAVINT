# NAVINT - Product Backlog

**Project:** NAVINT Maritime Intelligence Suite  
**Version:** 1.1 (Unified UI Edition)

---

## 1. EPIC: Core Infrastructure & Setup
| ID | Title | Priority | Status |
|----|-------|----------|--------|
| EB-001 | Local Environment Setup (`build.cmd`) | P0 | ✅ DONE |
| EB-002 | Database Schema (SQLite/SQLModel) | P0 | ✅ DONE |
| EB-003 | Backend Foundation (FastAPI) | P0 | ✅ DONE |

---

## 2. EPIC: Unified User Interface (Next.js)
| ID | Title | Priority | Status |
|----|-------|----------|--------|
| UI-001 | Premium Operational Landing Page | P0 | ✅ DONE |
| UI-002 | Integrated Map Visualization | P0 | TO DO |
| UI-003 | Analytics & Risk Scoring Panel | P1 | TO DO |
| UI-004 | Alert Management Workspace | P0 | TO DO |

---

## 3. EPIC: Data Ingestion & Intelligence
| ID | Title | Priority | Status |
|----|-------|----------|--------|
| DI-001 | Async AIS NMEA Ingestor | P0 | TO DO |
| DI-002 | Multi-factor Risk Engine | P0 | TO DO |
| DI-003 | Corporate Relationship Crawler | P1 | TO DO |

---

## 4. EPIC: Reporting & Audit
| ID | Title | Priority | Status |
|----|-------|----------|--------|
| RC-001 | Integrated Audit Trail View | P1 | TO DO |
| RC-002 | Export Engine (PDF/CSV/KML) | P1 | TO DO |

---

## 5. REFINEMENT NOTES
- **Constraint**: Consolidate all "Analytics" previously planned for Streamlit into the Next.js Analytics Panel.
- **Goal**: Sub-8GB RAM footprint.
