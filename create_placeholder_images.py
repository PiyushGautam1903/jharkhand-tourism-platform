#!/usr/bin/env python3
"""
Script to create placeholder images for Jharkhand tourism places.
This creates simple colored images with text overlays as placeholders.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create media/places directory if it doesn't exist
os.makedirs('media/places', exist_ok=True)

# Tourism places with their details
places = [
    {'name': 'Hundru Falls', 'filename': 'hundru_falls.jpg', 'color': (65, 105, 225)},  # Royal Blue
    {'name': 'Baidyanath Temple, Deoghar', 'filename': 'baidyanath_temple.jpg', 'color': (255, 140, 0)},  # Dark Orange
    {'name': 'Netarhat', 'filename': 'netarhat.jpg', 'color': (34, 139, 34)},  # Forest Green
    {'name': 'Betla National Park', 'filename': 'betla_national_park.jpg', 'color': (46, 125, 50)},  # Dark Green
    {'name': 'Rock Garden, Ranchi', 'filename': 'rock_garden.jpg', 'color': (156, 39, 176)},  # Purple
    {'name': 'Jonha Falls', 'filename': 'jonha_falls.jpg', 'color': (3, 169, 244)},  # Light Blue
    {'name': 'Jagannath Temple, Ranchi', 'filename': 'jagannath_temple.jpg', 'color': (255, 193, 7)},  # Amber
    {'name': 'Jamshedpur', 'filename': 'jamshedpur.jpg', 'color': (96, 125, 139)},  # Blue Grey
    {'name': 'Hazaribagh National Park', 'filename': 'hazaribagh_national_park.jpg', 'color': (76, 175, 80)},  # Green
    {'name': 'Ranchi Hill (Pahari Mandir)', 'filename': 'ranchi_hill.jpg', 'color': (255, 87, 34)},  # Deep Orange
    {'name': 'Dassam Falls', 'filename': 'dassam_falls.jpg', 'color': (33, 150, 243)},  # Blue
    {'name': 'Palamu Tiger Reserve', 'filename': 'palamu_tiger_reserve.jpg', 'color': (255, 152, 0)},  # Orange
]

# Image dimensions
width, height = 800, 600

def create_placeholder_image(place_info):
    """Create a placeholder image for a tourism place."""
    # Create a new image with the specified color
    img = Image.new('RGB', (width, height), color=place_info['color'])
    draw = ImageDraw.Draw(img)
    
    # Try to use a larger font, fall back to default if not available
    try:
        # Try to load a system font
        font_large = ImageFont.truetype("arial.ttf", 48)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except:
        try:
            # Try alternative system fonts
            font_large = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 48)
            font_small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 24)
        except:
            # Fall back to default font
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()
    
    # Add place name text
    place_name = place_info['name']
    
    # Calculate text position (centered)
    bbox = draw.textbbox((0, 0), place_name, font=font_large)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Add text shadow for better visibility
    shadow_offset = 3
    draw.text((x + shadow_offset, y + shadow_offset), place_name, fill=(0, 0, 0), font=font_large)
    draw.text((x, y), place_name, fill=(255, 255, 255), font=font_large)
    
    # Add "Jharkhand Tourism" subtitle
    subtitle = "Jharkhand Tourism"
    bbox_sub = draw.textbbox((0, 0), subtitle, font=font_small)
    sub_width = bbox_sub[2] - bbox_sub[0]
    
    x_sub = (width - sub_width) // 2
    y_sub = y + text_height + 20
    
    draw.text((x_sub + 2, y_sub + 2), subtitle, fill=(0, 0, 0), font=font_small)
    draw.text((x_sub, y_sub), subtitle, fill=(255, 255, 255), font=font_small)
    
    # Save the image
    filepath = f'media/places/{place_info["filename"]}'
    img.save(filepath, 'JPEG', quality=85)
    print(f"Created: {filepath}")

# Create all placeholder images
print("Creating placeholder images for Jharkhand tourism places...")
for place in places:
    create_placeholder_image(place)

print(f"\nSuccessfully created {len(places)} placeholder images!")
print("Images saved to: media/places/")