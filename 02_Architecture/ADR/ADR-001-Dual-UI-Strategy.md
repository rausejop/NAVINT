# ADR-001: Dual-UI Strategy (Next.js & Streamlit)

## Status
Accepted

## Context
The NAVINT platform requires both a highly interactive, custom-designed operational map (Next.js) and a flexible, iterative data science dashboard for risk modeling and bulk analysis (Streamlit).

## Decision
We will implement a multi-UI approach:
1.  **Next.js (Port 3000)**: Serves as the primary operational workspace. Chosen for its performance, ability to handle complex map interactivity (Leaflet/Mapbox), and premium UX/UI capabilities.
2.  **Streamlit (Port 8501)**: Serves as the technical analytics and configuration interface. Chosen for its rapid development cycle for data-heavy dashboards and seamless integration with Python-based logic/models.

## Consequences
- **Pros**: Clear separation of concerns between operational monitoring and analytical modeling; faster prototyping of new analytical features in Streamlit.
- **Cons**: Increased overhead in maintaining two frontend codebases; requires managing cross-origin requests (CORS) between APIs and both UIs.
- **Mitigation**: Shared FastAPI backend ensures a single source of truth for both interfaces.
