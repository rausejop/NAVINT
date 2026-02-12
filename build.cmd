@echo off
REM NAVINT - Automated Build & Setup Script
REM Standard: CONF23-STD-SDLC-NAVMIL
SETLOCAL EnableDelayedExpansion

echo ============================================================
echo [NAVINT] - Initializing Standalone Local Platform (Unified Next.js)
echo ============================================================

:: 1. VERIFY PYTHON VERSION
echo [1/5] Checking Python version...
python --version 2>&1 | findstr /R "3.14" >nul
if %errorlevel% neq 0 (
    echo [ERROR] Python 3.14.2 is required. Found:
    python --version
    exit /b 1
)

:: 2. SETUP VIRTUAL ENVIRONMENT
echo [2/5] Setting up virtual environment (.venv)...
if not exist .venv (
    python -m venv .venv
)
call .venv\Scripts\activate

:: 3. INSTALL BACKEND DEPENDENCIES
echo [3/5] Installing dependencies (FastAPI, SQLModel, etc.)...
python -m pip install --upgrade pip
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo [INFO] requirements.txt not found. Creating default...
    echo fastapi > requirements.txt
    echo uvicorn >> requirements.txt
    echo loguru >> requirements.txt
    echo sqlmodel >> requirements.txt
    echo pydantic-settings >> requirements.txt
    pip install -r requirements.txt
)

:: 4. SETUP FRONTEND (NEXT.JS)
echo [4/5] Initializing Unified Next.js Frontend...
cd frontend
if exist package.json (
    echo [INFO] Installing NPM dependencies...
    REM call npm install (Disabled for non-node environments)
)
cd ..

:: 5. INITIALIZE DATABASE
echo [5/5] Initializing SQLite Database and Seeding Data...
python -m app.init_db
python -m app.seed_data

echo ============================================================
echo [NAVINT] Build complete.
echo To start the platform:
echo 1. Backend:  uvicorn app.main:app --reload
echo 2. Frontend: cd frontend ^& npm run dev
echo ============================================================

pause




