@echo off
title AgentGrid All-in-One Runner

:: 1. Start Python Backend in background
start "Backend" /min cmd /c "cd /d "%~dp0backend" && "%~dp0backend\venv\Scripts\python.exe" -m uvicorn main:app --host 0.0.0.0 --port 8000"

:: 2. Start Frontend Dev Server in background
start "Frontend" /min cmd /c "cd /d "%~dp0frontend" && npm run dev"

:: 3. Wait 3 seconds and open the app in your browser
ping 127.0.0.1 -n 4 >nul
start "" http://localhost:5173

exit