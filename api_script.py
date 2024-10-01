import os
from datetime import date

import requests
from dotenv import load_dotenv

load_dotenv()

# APOD - Astronomy Picture of the Day 
apod_url = "https://api.nasa.gov/planetary/apod"
# get your own from https://api.nasa.gov/
api_key = os.getenv("API_KEY")

today = date.today()
images_folder = "photos"

if not os.path.exists(images_folder):
    os.makedirs(images_folder)

params = {
    "api_key": api_key,
    #"date": f"{today.year}-{today.month}-{today.day}"
    "date": "2022-01-1"
    }

response = requests.get(apod_url, params=params)

print(response.text)
