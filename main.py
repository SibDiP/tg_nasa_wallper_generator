import os
from dotenv import load_dotenv


from nasa_apod_api_downloader import nasa_apod_api_downloader
from image_cropper import image_cropper
from utils import utils

load_dotenv()

IMAGES_DOWNLOAD_PATH = os.getenv("IMAGES_DOWNLOAD_PATH")
IMAGES_CROPPED_PATH = os.getenv("IMAGES_CROPPED_PATH")

utils.create_images_folder(IMAGES_DOWNLOAD_PATH)
downloaded_file_name = nasa_apod_api_downloader.download_apod_image(IMAGES_DOWNLOAD_PATH)
image_cropper.crop_image(IMAGES_DOWNLOAD_PATH + "/" + downloaded_file_name, IMAGES_CROPPED_PATH + "/" + downloaded_file_name)
