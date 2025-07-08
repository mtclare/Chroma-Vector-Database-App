@echo off
echo ========================================
echo    Email Vector Database
echo    Local Email Retrieval App
echo ========================================
echo.

echo Installing dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to install dependencies.
    echo Please make sure Python and pip are installed.
    pause
    exit /b 1
)

echo.
echo Fixing dependency compatibility issues...
python fix_dependencies.py

echo.
echo Dependencies installed successfully!
echo.
echo Starting the application...
echo Web interface will be available at:
echo   • http://localhost:8000
echo   • http://127.0.0.1:8000
echo Press Ctrl+C to stop the server
echo.

python run.py

pause 