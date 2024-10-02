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

def download_apod_image(target_date: date = None) -> None:
    # APOD - Astronomy Picture of the Day 
    apod_url = "https://api.nasa.gov/planetary/apod"
    # get your own api_keyfrom https://api.nasa.gov/ and put in .env file in root.
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if target_date is None:
        # Take yesterday becouse of the timezone differences. 
        yesterday = date.today() - timedelta(days=1)
        target_date = yesterday

    params = {
        "api_key": api_key,
        #"date": f"{target_date.year}-{target_date.month}-{target_date.day}"
        "date": "2022-01-1"
        }

    response = requests.get(apod_url, params=params)
    print(response.text)

    if response.status_code == 200:
        if is_image(response.json()['media_type']):
            hd_image_url = response.json()["hdurl"]
            response = requests.get(hd_image_url)
            
            with open(f"{IMAGES_FOLDER_PATH}/{target_date}.jpg", "wb") as f:
                f.write(response.content)
    else:
        print(f"Operation failed. Status code: {response.status_code}.")

def main() -> None:
    create_images_folder()
    download_apod_image()

if __name__ == "__main__":
    main()
