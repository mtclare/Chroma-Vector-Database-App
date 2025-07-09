#!/bin/bash

# Email Vector Database - Automated Deployment Script
# This script automates the deployment process for Render

set -e  # Exit on any error

echo "🚀 Email Vector Database - Automated Deployment"
echo "=============================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Git is installed
if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install Git first."
    exit 1
fi

# Check if we're in a Git repository
if [ ! -d ".git" ]; then
    print_status "Initializing Git repository..."
    git init
    print_success "Git repository initialized"
fi

# Check if remote repository is configured
if ! git remote get-url origin &> /dev/null; then
    print_warning "No remote repository configured."
    echo ""
    echo "To deploy to Render, you need to:"
    echo "1. Create a repository on GitHub/GitLab"
    echo "2. Add it as remote: git remote add origin YOUR_REPO_URL"
    echo "3. Push your code: git push -u origin main"
    echo ""
    echo "Or you can manually deploy by:"
    echo "1. Going to https://render.com"
    echo "2. Creating a new Web Service"
    echo "3. Connecting your repository"
    echo "4. Using these settings:"
    echo "   - Build Command: pip install -r requirements.txt"
    echo "   - Start Command: uvicorn app:app --host 0.0.0.0 --port \$PORT"
    echo ""
    exit 0
fi

# Add all files to Git
print_status "Adding files to Git..."
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    print_warning "No changes to commit. All files are up to date."
else
    print_status "Committing changes..."
    git commit -m "Deploy Email Vector Database to Render - $(date)"
    print_success "Changes committed"
fi

# Push to remote repository
print_status "Pushing to remote repository..."
if git push; then
    print_success "Code pushed to remote repository"
else
    print_error "Failed to push to remote repository"
    echo ""
    echo "Please check your Git configuration and try again."
    exit 1
fi

echo ""
print_success "Deployment files are ready!"
echo ""
echo "📋 Next Steps:"
echo "=============="
echo ""
echo "1. 🌐 Go to https://render.com and sign up/login"
echo "2. 🔗 Connect your GitHub/GitLab repository"
echo "3. ➕ Click 'New +' and select 'Web Service'"
echo "4. ⚙️  Configure your service:"
echo "   - Name: email-vector-database"
echo "   - Environment: Python 3"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: uvicorn app:app --host 0.0.0.0 --port \$PORT"
echo "5. 🚀 Click 'Create Web Service'"
echo ""
echo "⏱️  Deployment will take 2-5 minutes"
echo "🌍 Your app will be available at: https://your-app-name.onrender.com"
echo ""
echo "📊 Monitor deployment in the Render dashboard"
echo "🔍 Check logs if there are any issues"
echo ""
print_success "Happy deploying! 🎉" 