#!/usr/bin/env python3
"""
Server Test Script
Tests if the Email Vector Database server is running and accessible.
"""

import requests
import time
import sys

def test_server():
    """Test if the server is running and accessible"""
    print("🧪 Testing server connectivity...")
    print()
    
    urls_to_test = [
        "http://localhost:8000",
        "http://127.0.0.1:8000"
    ]
    
    for url in urls_to_test:
        print(f"Testing {url}...")
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ {url} - Server is running!")
                print(f"   Status Code: {response.status_code}")
                print(f"   Content Length: {len(response.text)} characters")
                return True
            else:
                print(f"⚠️  {url} - Server responded with status {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ {url} - Connection refused. Server might not be running.")
        except requests.exceptions.Timeout:
            print(f"⏰ {url} - Request timed out.")
        except Exception as e:
            print(f"❌ {url} - Error: {e}")
        print()
    
    return False

def check_common_issues():
    """Check for common issues"""
    print("🔍 Checking for common issues...")
    print()
    
    # Check if port 8000 is in use
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', 8000))
    sock.close()
    
    if result == 0:
        print("✅ Port 8000 is accessible")
    else:
        print("❌ Port 8000 is not accessible")
        print("   Make sure the server is running with: python run.py")
    
    print()
    print("💡 Troubleshooting tips:")
    print("   1. Make sure you ran: python run.py")
    print("   2. Try accessing: http://localhost:8000")
    print("   3. Check if another app is using port 8000")
    print("   4. Try a different port in app.py if needed")

if __name__ == "__main__":
    print("=" * 50)
    print("Email Vector Database - Server Test")
    print("=" * 50)
    print()
    
    if test_server():
        print("🎉 Server is running correctly!")
        print("🌐 Open your browser and go to: http://localhost:8000")
    else:
        print("❌ Server test failed.")
        check_common_issues() 