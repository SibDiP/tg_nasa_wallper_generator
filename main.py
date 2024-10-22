import os
from dotenv import load_dotenv


from nasa_apod_api_downloader import nasa_apod_api_downloader
from utils import utils

load_dotenv()

IMAGES_OUTPUT_DIR = os.getenv("IMAGES_OUTPUT_DIR")

utils.create_images_folder(IMAGES_OUTPUT_DIR)
nasa_apod_api_downloader.download_apod_image()