import os
from datetime import date, timedelta

import requests
from dotenv import load_dotenv

IMAGES_FOLDER_PATH = "./photos"

def is_image(media_type: str) -> bool:
    return media_type == 'image'

def create_images_folder() -> None:
    if not os.path.exists(IMAGES_FOLDER_PATH):
        os.makedirs(IMAGES_FOLDER_PATH)

load_dotenv()

# APOD - Astronomy Picture of the Day 
apod_url = "https://api.nasa.gov/planetary/apod"
# get your own from https://api.nasa.gov/
api_key = os.getenv("API_KEY")

# Take yesterday becouse of the timezone differences. 
yesterday = date.today() - timedelta(days=1)
params = {
    "api_key": api_key,
    "date": f"{yesterday.year}-{yesterday.month}-{yesterday.day}"
    #"date": "2022-01-1"
    }

response = requests.get(apod_url, params=params)
print(response.text)

create_images_folder()

if response.status_code == 200:
    if is_image(response.json()['media_type']):
        hd_image_url = response.json()["hdurl"]
        response = requests.get(hd_image_url)
        
        with open(f"{IMAGES_FOLDER_PATH}/{yesterday}.jpg", "wb") as f:
            f.write(response.content)
else:
    print(f"Operation failed. Status code: {response.status_code}.")

    
