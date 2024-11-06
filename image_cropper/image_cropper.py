from PIL import Image
import os
import logging

logging.basicConfig(level=logging.INFO)


def crop_image(image_path: str, output_path: str) -> None:

    """
    Crops the given image to 9:16 ratio and saves it to the output path.

    Args:
        image_path: The path to the image to be cropped.
        output_path: The path where the cropped image will be saved.

    Returns:
        None
    """
    FULL_CROPPED_FILE_PATH = output_path


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
        cropped_image.save(FULL_CROPPED_FILE_PATH)
        logging.info(f"Cropped image saved to: {FULL_CROPPED_FILE_PATH}")
    except FileNotFoundError:
        logging.error(f"Can't save cropped image. Output file path not found: {FULL_CROPPED_FILE_PATH}")
        exit()
