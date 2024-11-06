

[![Python 3.12](https://badgen.net/badge/Python/3.12/blue)](https://www.python.org/downloads/release/python-312/)
[![Pillow 10.4](https://badgen.net/badge/Pillow/10.4/green)](https://pypi.org/project/Pillow/)
[![JSON](https://badgen.net/badge/JSON//API/green)](https://www.json.org/)


# tg_nasa_wallpaper_generator
Python script for downloading nice images from [nasa APOD API](https://api.nasa.gov/), and cropping them to 9:16 ratio (good for smartphone wallpapers).



Python script which:
1. Downloads images from [NASA APOD API](https://api.nasa.gov/).
2. Resizes it to 9:16 ratio.
3. Saves the cropped image.


## How to use
1. Install requirements.txt.
2. Fill example.env with your NASA API Key.
3. Rename "example.env" to ".env".
4. Run main.py


## Settings
By default, the original image will be saved as ./photos/{date: XXXX-XX-XX.png}. The cropped image will be saved as ./cropped/{date: XXXX-XX-XX.png}. It can be changed in the .env file.


