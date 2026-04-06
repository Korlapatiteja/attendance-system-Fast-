@echo off
echo Starting Fast Attendance System...

:: Start Backend
start "Backend" cmd /k "cd /d "%~dp0backend" && "%~dp0venv2\Scripts\activate.bat" && uvicorn main:app --reload"

:: Wait 3 seconds for backend to start
timeout /t 3 /nobreak > nul

:: Start Frontend
start "Frontend" cmd /k "cd /d "%~dp0frontend" && npm start"

echo Both servers are starting...
echo Backend: http://127.0.0.1:8000
echo Frontend: http://localhost:3000
