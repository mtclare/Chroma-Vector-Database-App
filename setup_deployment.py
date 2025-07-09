#!/usr/bin/env python3
"""
Email Vector Database - Automated Deployment Setup
This script automates all the deployment preparation steps for Render.
"""

import os
import subprocess
import sys
import json
from datetime import datetime

def print_header():
    """Print deployment header"""
    print("🚀 Email Vector Database - Automated Deployment Setup")
    print("=" * 55)
    print()

def print_step(step_num, title):
    """Print a step header"""
    print(f"📋 Step {step_num}: {title}")
    print("-" * 40)

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return True
        else:
            print(f"❌ {description} failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} failed: {str(e)}")
        return False

def check_git():
    """Check if Git is installed and configured"""
    print_step(1, "Checking Git Installation")
    
    # Check if Git is installed
    if not run_command("git --version", "Checking Git installation"):
        print("\n❌ Git is not installed. Please install Git first:")
        print("   Download from: https://git-scm.com/downloads")
        return False
    
    # Check if we're in a Git repository
    if not os.path.exists(".git"):
        print("\n📁 Initializing Git repository...")
        if run_command("git init", "Initializing Git repository"):
            print("✅ Git repository initialized")
        else:
            return False
    
    # Check if remote is configured
    result = subprocess.run("git remote get-url origin", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("\n⚠️  No remote repository configured.")
        print("\n📋 To complete deployment, you need to:")
        print("   1. Create a repository on GitHub/GitLab")
        print("   2. Add it as remote: git remote add origin YOUR_REPO_URL")
        print("   3. Run this script again")
        return False
    
    print("✅ Git is properly configured")
    return True

def prepare_files():
    """Prepare all necessary files for deployment"""
    print_step(2, "Preparing Deployment Files")
    
    # Check if all required files exist
    required_files = [
        "app.py",
        "requirements.txt",
        "render.yaml",
        ".gitignore"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All deployment files are present")
    return True

def commit_changes():
    """Commit all changes to Git"""
    print_step(3, "Committing Changes to Git")
    
    # Add all files
    if not run_command("git add .", "Adding files to Git"):
        return False
    
    # Check if there are changes to commit
    result = subprocess.run("git diff --cached --quiet", shell=True, capture_output=True)
    if result.returncode == 0:
        print("ℹ️  No changes to commit. All files are up to date.")
        return True
    
    # Commit changes
    commit_message = f"Deploy Email Vector Database to Render - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    if run_command(f'git commit -m "{commit_message}"', "Committing changes"):
        print("✅ Changes committed successfully")
        return True
    
    return False

def push_to_remote():
    """Push changes to remote repository"""
    print_step(4, "Pushing to Remote Repository")
    
    if run_command("git push", "Pushing to remote repository"):
        print("✅ Code pushed to remote repository")
        return True
    
    print("❌ Failed to push to remote repository")
    print("   Please check your Git configuration and try again.")
    return False

def show_deployment_instructions():
    """Show final deployment instructions"""
    print_step(5, "Deployment Instructions")
    
    print("🎉 All deployment files are ready!")
    print()
    print("📋 Next Steps for Render Deployment:")
    print("====================================")
    print()
    print("1. 🌐 Go to https://render.com and sign up/login")
    print("2. 🔗 Connect your GitHub/GitLab repository")
    print("3. ➕ Click 'New +' and select 'Web Service'")
    print("4. ⚙️  Configure your service with these settings:")
    print()
    print("   📝 Service Configuration:")
    print("   - Name: email-vector-database")
    print("   - Environment: Python 3")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: uvicorn app:app --host 0.0.0.0 --port $PORT")
    print()
    print("5. 🚀 Click 'Create Web Service'")
    print()
    print("⏱️  Deployment will take 2-5 minutes")
    print("🌍 Your app will be available at: https://your-app-name.onrender.com")
    print()
    print("📊 Monitor deployment in the Render dashboard")
    print("🔍 Check logs if there are any issues")
    print()
    print("⚠️  Important Notes:")
    print("===================")
    print("• Free tier has ephemeral storage (data lost on restart)")
    print("• For production, consider paid plan with persistent disk")
    print("• Monitor memory usage in Render dashboard")
    print()
    print("🎯 Your Email Vector Database is ready for deployment!")
    print("   Happy deploying! 🚀")

def main():
    """Main deployment setup function"""
    print_header()
    
    # Step 1: Check Git
    if not check_git():
        return
    
    # Step 2: Prepare files
    if not prepare_files():
        return
    
    # Step 3: Commit changes
    if not commit_changes():
        return
    
    # Step 4: Push to remote
    if not push_to_remote():
        return
    
    # Step 5: Show instructions
    show_deployment_instructions()

if __name__ == "__main__":
    main() 