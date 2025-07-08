#!/usr/bin/env python3
"""
Comprehensive Dependency Fix
This script completely removes and reinstalls all problematic dependencies in the correct order.
"""

import subprocess
import sys
import os

def fix_all_dependencies():
    """Fix all dependency compatibility issues"""
    print("🔧 Comprehensive dependency fix...")
    print("This will remove and reinstall all problematic packages.")
    print()
    
    try:
        # Step 1: Remove all problematic packages
        print("📦 Step 1: Removing problematic packages...")
        packages_to_remove = [
            "numpy",
            "huggingface-hub", 
            "sentence-transformers",
            "transformers",
            "torch"
        ]
        
        for package in packages_to_remove:
            print(f"   Removing {package}...")
            subprocess.run([sys.executable, "-m", "pip", "uninstall", package, "-y"], 
                         capture_output=True)
        
        # Step 2: Install compatible versions in correct order
        print("\n📦 Step 2: Installing compatible versions...")
        
        # Install numpy first
        print("   Installing numpy==1.24.3...")
        subprocess.run([sys.executable, "-m", "pip", "install", "numpy==1.24.3"])
        
        # Install huggingface-hub
        print("   Installing huggingface-hub==0.16.4...")
        subprocess.run([sys.executable, "-m", "pip", "install", "huggingface-hub==0.16.4"])
        
        # Install torch
        print("   Installing torch...")
        subprocess.run([sys.executable, "-m", "pip", "install", "torch>=1.9.0"])
        
        # Install transformers
        print("   Installing transformers...")
        subprocess.run([sys.executable, "-m", "pip", "install", "transformers>=4.21.0"])
        
        # Install sentence-transformers last
        print("   Installing sentence-transformers==2.2.2...")
        subprocess.run([sys.executable, "-m", "pip", "install", "sentence-transformers==2.2.2"])
        
        # Step 3: Install other requirements
        print("\n📦 Step 3: Installing other requirements...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        
        print("\n✅ All dependencies fixed successfully!")
        print("💡 You can now run the application without errors.")
        
    except Exception as e:
        print(f"\n❌ Error during dependency fix: {e}")
        print("\n💡 Manual fix instructions:")
        print("1. pip uninstall numpy huggingface-hub sentence-transformers transformers torch -y")
        print("2. pip install numpy==1.24.3")
        print("3. pip install huggingface-hub==0.16.4")
        print("4. pip install torch>=1.9.0")
        print("5. pip install transformers>=4.21.0")
        print("6. pip install sentence-transformers==2.2.2")

def test_imports():
    """Test if the imports work correctly"""
    print("\n🧪 Testing imports...")
    
    try:
        import numpy as np
        print("✅ NumPy imported successfully")
        
        import huggingface_hub
        print("✅ huggingface_hub imported successfully")
        
        from sentence_transformers import SentenceTransformer
        print("✅ sentence_transformers imported successfully")
        
        print("\n🎉 All imports working correctly!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Comprehensive Dependency Fix")
    print("=" * 60)
    print()
    
    response = input("This will remove and reinstall all dependencies. Continue? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        exit()
    
    fix_all_dependencies()
    
    # Test the imports
    if test_imports():
        print("\n🚀 Ready to run the application!")
        print("Run: python run.py")
    else:
        print("\n⚠️  Some imports still failed. Please check the manual instructions above.") 