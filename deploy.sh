#!/bin/bash

# Email Vector Database - Deployment Script
# This script helps with local testing and deployment preparation

echo "🚀 Email Vector Database - Deployment Script"
echo "=============================================="

# Function to build and test locally
test_local() {
    echo "📦 Building Docker image..."
    docker build -t email-vector-db .
    
    echo "🧪 Testing locally with Docker Compose..."
    docker-compose up --build -d
    
    echo "⏳ Waiting for application to start..."
    sleep 10
    
    echo "🔍 Testing health endpoint..."
    curl -f http://localhost:8000/health || echo "❌ Health check failed"
    
    echo "🌐 Application should be running at http://localhost:8000"
    echo "📊 To view logs: docker-compose logs -f"
    echo "🛑 To stop: docker-compose down"
}

# Function to clean up
cleanup() {
    echo "🧹 Cleaning up..."
    docker-compose down
    docker system prune -f
    echo "✅ Cleanup complete"
}

# Function to show help
show_help() {
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  test     - Build and test locally with Docker"
    echo "  clean    - Clean up Docker containers and images"
    echo "  help     - Show this help message"
    echo ""
    echo "For Railway deployment:"
    echo "  1. Install Railway CLI: npm install -g @railway/cli"
    echo "  2. Login: railway login"
    echo "  3. Deploy: railway up"
}

# Main script logic
case "${1:-help}" in
    "test")
        test_local
        ;;
    "clean")
        cleanup
        ;;
    "help"|*)
        show_help
        ;;
esac 