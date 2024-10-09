# **NASA APOD API Downloader**

### Description

This script allows to download images from the NASA APOD (Astronomy Picture of the Day) API.

### Usage

Add your NASA api_key to 'example.env' and rename it to '.env'.

### Functions

#### download_apod_image(target_date: date = None) -> None

Downloads an image from the NASA APOD API to IMAGES_OUTPUT_DIR.

- `date`: The date of the target image in date format. Take yesterday by defoult because of the timezone difference issues (it can be yesterday in USA timezone).

### Constants
Stored in .env.

- `API_KEY`: Default NASA APOD API key.
- `API_URL`: URL of the NASA APOD API.
- `IMAGES_OUTPUT_DIR`: Directory for saved photos. './photos' by defoult.

### Author

- Dmitrii Pivnev (sibdip)