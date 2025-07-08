#!/usr/bin/env python3
"""
Email Vector Database - Startup Script
A simple script to run the email vector database application.
"""

import uvicorn
import sys
import os

def main():
    """Start the email vector database application"""
    print("🚀 Starting Email Vector Database...")
    print("📧 Local email retrieval with semantic search")
    print("🌐 Web interface will be available at:")
    print("   • http://localhost:8000")
    print("   • http://127.0.0.1:8000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Run the FastAPI application
        uvicorn.run(
            "app:app",
            host="0.0.0.0",
            port=8000,
            reload=True,  # Auto-reload on code changes
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 Shutting down Email Vector Database...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting the application: {e}")
        print("💡 Make sure you have installed all dependencies:")
        print("   pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main() 