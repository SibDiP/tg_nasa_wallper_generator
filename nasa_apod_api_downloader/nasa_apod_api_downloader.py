import os
from datetime import date, timedelta
import json
import logging

import requests
from dotenv import load_dotenv

from utils import utils

load_dotenv()

IMAGES_OUTPUT_DIR = os.getenv("IMAGES_OUTPUT_DIR")
# APOD - Astronomy Picture of the Day 
APOD_URL = os.getenv("APOD_URL")
# get your own api_keyfrom https://api.nasa.gov/ and put in .env file in root dir.
API_KEY = os.getenv("API_KEY")

logging.basicConfig(level=logging.INFO)

def is_image(media_type: str) -> bool:
    return media_type == 'image'

def download_apod_image(images_download_path: str, target_date: date = None,) -> None:
    """
    Downloads an image from the NASA APOD api for the given date.

    If target_date is None, the function will take yesterday's date because of the timezone 
    differenceissues (it can be yesterday in USA timezone).

    The function logs the status of the operation and the downloaded file.

    :param target_date: The date for which the image is downloaded
    :type target_date: date
    :return: None
    """
    if target_date is None:
        # Take yesterday becouse of the timezone difference issues (it can be yesterday in USA timezone). 
        yesterday = date.today() - timedelta(days=1)
        target_date = yesterday
        logging.info(f"Target date is {target_date}")

    params = {
        "api_key": API_KEY,
        "date": f"{target_date.year}-{target_date.month}-{target_date.day}"
        #"date": "2022-01-1"
        }

    response = requests.get(APOD_URL, params=params)
    media_type = response.json()['media_type']
    logging.info(f"Response:\n{json.dumps(response.json(), indent=4)}")


    if response.status_code == 200:
        if is_image(media_type):
            hd_image_url = response.json()["hdurl"]
            response = requests.get(hd_image_url)
            
            with open(f"{images_download_path}/{target_date}.jpg", "wb") as f:
                f.write(response.content)
                logging.info(f"Downloaded image at {target_date}.")
        else:
            logging.warning(f"Probobly no picture at {target_date}.\n    >Media type: {media_type} \n    >Response code: {response.status_code}")
    else:
        logging.warning(f"Operation failed. Status code: {response.status_code}.")
