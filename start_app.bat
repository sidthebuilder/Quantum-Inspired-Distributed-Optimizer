@echo off
echo ==============================================
echo   QuasiQ Optimizer - One-Click Launcher
echo ==============================================
echo.
echo [1/3] Checking Docker...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Docker is not installed or not in PATH.
    pause
    exit /b
)

echo [2/3] Building and Starting Services...
docker-compose up --build -d

echo [3/3] Deployment Complete!
echo.
echo Frontend: http://localhost:3000
echo Backend:  http://localhost:8000/docs
echo.
echo Logs are streaming below (Ctrl+C to stop trailing logs)...
docker-compose logs -f
