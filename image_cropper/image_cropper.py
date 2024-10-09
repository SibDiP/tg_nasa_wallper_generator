from PIL import Image
import os

def crop_image(image_path: str, output_path: str) -> None:

    image = Image.open(image_path)
    width, height = image.size
    
    # New 9:16 picture size
    new_width = int(height * 9 / 16)
    new_height = height
    
    # Calculate crop box
    left = (width - new_width) // 2
    top = (height - new_height) // 2
    right = left + new_width
    bottom = top + new_height
    
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)
