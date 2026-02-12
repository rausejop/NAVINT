# NAVINT - Definition of Done (DoD)

**Project:** NAVINT Maritime Intelligence Suite  
**Standard Compliance:** CONF23-STD-SDLC-NAVMIL  

---

## 1. CODE QUALITY
- [ ] Code follows **SOLID** and **DRY** principles.
- [ ] **Python 3.14.2** type hints and Google-style docstrings are present.
- [ ] No hardcoded configuration; all settings loaded from environment variables or local `.env`.
- [ ] `asyncio` is used for all I/O and database calls.

## 2. SECURITY & COMPLIANCE
- [ ] **OWASP Top 10 2025** early mitigation implemented.
- [ ] All inputs sanitized via Pydantic/Next.js validation.
- [ ] **loguru** logging is structured (JSON) and contains no personal data.
- [ ] Services restricted to **localhost** access.

## 3. TESTING
- [ ] Unit tests pass for the specific logic/component.
- [ ] Manual verification in the local web interface (Next.js/Streamlit).
- [ ] Memory footprint verified to be under 8GB overhead.

## 4. DOCUMENTATION
- [ ] Relevant **ADR** generated for any non-trivial architectural decision.
- [ ] API documentation (Swagger/FastAPI) is up to date.
- [ ] Product Backlog updated with the completion status.

## 5. REPOSITORY & BUILD
- [ ] Code integrated into the local repository.
- [ ] `build.cmd` updated if new dependencies or environment steps are added.
- [ ] `requirements.txt` updated (no `uv`).
