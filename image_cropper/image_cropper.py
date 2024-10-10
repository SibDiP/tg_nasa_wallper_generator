from PIL import Image
import os
import logging

logging.basicConfig(level=logging.INFO)


def crop_image(image_path: str, output_path: str) -> None:

    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        logging.error(f"Original image file not found: {image_path}")
        exit()

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
    try:
        cropped_image.save(output_path)
    except FileNotFoundError:
        logging.error(f"Can't save cropped image. Output file path not found: {output_path}")
        exit()

crop_image("photos/CometA3_Mueras_1872.jpg", "photoss/cropped.jpg")