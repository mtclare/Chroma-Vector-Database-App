#!/usr/bin/env python3
"""
Dependency Compatibility Fix
This script fixes compatibility issues with NumPy and huggingface_hub.
"""

import subprocess
import sys

def fix_compatibility_issues():
    """Fix compatibility issues with dependencies"""
    print("🔧 Fixing dependency compatibility issues...")
    
    try:
        # Fix NumPy compatibility
        print("📦 Checking NumPy version...")
        result = subprocess.run([sys.executable, "-m", "pip", "show", "numpy"], 
                              capture_output=True, text=True)
        
        if "Version: 2." in result.stdout:
            print("📦 Uninstalling NumPy 2.0+...")
            subprocess.run([sys.executable, "-m", "pip", "uninstall", "numpy", "-y"])
            print("📦 Installing NumPy 1.24.3 (compatible version)...")
            subprocess.run([sys.executable, "-m", "pip", "install", "numpy==1.24.3"])
        
        # Fix huggingface_hub compatibility
        print("📦 Checking huggingface_hub version...")
        result = subprocess.run([sys.executable, "-m", "pip", "show", "huggingface-hub"], 
                              capture_output=True, text=True)
        
        # Check if version is not 0.16.4 (our target version)
        if "Version: 0.16.4" not in result.stdout:
            print("📦 Uninstalling incompatible huggingface_hub...")
            subprocess.run([sys.executable, "-m", "pip", "uninstall", "huggingface-hub", "-y"])
            print("📦 Installing huggingface_hub 0.16.4 (compatible version)...")
            subprocess.run([sys.executable, "-m", "pip", "install", "huggingface-hub==0.16.4"])
        
        print("✅ All compatibility issues fixed!")
        print("💡 You can now run the application without errors.")
        
    except Exception as e:
        print(f"❌ Error fixing compatibility issues: {e}")
        print("💡 Try running: pip install numpy==1.24.3 huggingface-hub==0.16.4")

if __name__ == "__main__":
    print("=" * 50)
    print("Dependency Compatibility Fix")
    print("=" * 50)
    print()
    fix_compatibility_issues() 