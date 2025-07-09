@echo off
REM Email Vector Database - Automated Deployment Script for Windows
REM This script automates the deployment process for Render

echo 🚀 Email Vector Database - Automated Deployment
echo ==============================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed. Please install Git first.
    pause
    exit /b 1
)

REM Check if we're in a Git repository
if not exist ".git" (
    echo [INFO] Initializing Git repository...
    git init
    echo [SUCCESS] Git repository initialized
)

REM Check if remote repository is configured
git remote get-url origin >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] No remote repository configured.
    echo.
    echo To deploy to Render, you need to:
    echo 1. Create a repository on GitHub/GitLab
    echo 2. Add it as remote: git remote add origin YOUR_REPO_URL
    echo 3. Push your code: git push -u origin main
    echo.
    echo Or you can manually deploy by:
    echo 1. Going to https://render.com
    echo 2. Creating a new Web Service
    echo 3. Connecting your repository
    echo 4. Using these settings:
    echo    - Build Command: pip install -r requirements.txt
    echo    - Start Command: uvicorn app:app --host 0.0.0.0 --port $PORT
    echo.
    pause
    exit /b 0
)

REM Add all files to Git
echo [INFO] Adding files to Git...
git add .

REM Check if there are changes to commit
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo [WARNING] No changes to commit. All files are up to date.
) else (
    echo [INFO] Committing changes...
    git commit -m "Deploy Email Vector Database to Render - %date% %time%"
    echo [SUCCESS] Changes committed
)

REM Push to remote repository
echo [INFO] Pushing to remote repository...
git push
if %errorlevel% equ 0 (
    echo [SUCCESS] Code pushed to remote repository
) else (
    echo [ERROR] Failed to push to remote repository
    echo.
    echo Please check your Git configuration and try again.
    pause
    exit /b 1
)

echo.
echo [SUCCESS] Deployment files are ready!
echo.
echo 📋 Next Steps:
echo ==============
echo.
echo 1. 🌐 Go to https://render.com and sign up/login
echo 2. 🔗 Connect your GitHub/GitLab repository
echo 3. ➕ Click 'New +' and select 'Web Service'
echo 4. ⚙️  Configure your service:
echo    - Name: email-vector-database
echo    - Environment: Python 3
echo    - Build Command: pip install -r requirements.txt
echo    - Start Command: uvicorn app:app --host 0.0.0.0 --port $PORT
echo 5. 🚀 Click 'Create Web Service'
echo.
echo ⏱️  Deployment will take 2-5 minutes
echo 🌍 Your app will be available at: https://your-app-name.onrender.com
echo.
echo 📊 Monitor deployment in the Render dashboard
echo 🔍 Check logs if there are any issues
echo.
echo [SUCCESS] Happy deploying! 🎉
pause 