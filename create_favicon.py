#!/usr/bin/env python3
"""
Create a simple favicon.ico file for the Email Vector Database application
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_favicon():
    """Create a simple favicon with email/vector database theme"""
    
    # Create a 32x32 image with a blue background
    size = (32, 32)
    img = Image.new('RGBA', size, (41, 128, 185, 255))  # Blue background
    draw = ImageDraw.Draw(img)
    
    # Draw a simple email icon (envelope shape)
    # Envelope outline
    draw.polygon([(6, 12), (16, 6), (26, 12), (26, 26), (6, 26)], 
                 fill=(255, 255, 255, 255), outline=(255, 255, 255, 255))
    
    # Envelope flap
    draw.polygon([(6, 12), (16, 18), (26, 12)], 
                 fill=(255, 255, 255, 255), outline=(255, 255, 255, 255))
    
    # Add a small vector/database symbol (dots representing vectors)
    draw.ellipse([(20, 20), (24, 24)], fill=(255, 255, 255, 255))  # Top right dot
    draw.ellipse([(8, 20), (12, 24)], fill=(255, 255, 255, 255))   # Top left dot
    draw.ellipse([(14, 22), (18, 26)], fill=(255, 255, 255, 255))  # Center dot
    
    # Save as ICO file
    img.save('favicon.ico', format='ICO', sizes=[(32, 32)])
    print("✅ Favicon created successfully: favicon.ico")

if __name__ == "__main__":
    try:
        create_favicon()
    except ImportError:
        print("❌ PIL (Pillow) not installed. Installing...")
        os.system("pip install Pillow")
        create_favicon()
    except Exception as e:
        print(f"❌ Error creating favicon: {e}") 