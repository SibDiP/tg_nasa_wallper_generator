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

# utils.py
================

## Module Description

This module provides utility functions for creating directories.

## Functions

### `create_images_folder(dir: str) -> None`

Creates a directory at the specified path if it does not already exist.

#### Args

- `dir`: The path to the directory to be created.

#### Returns

- `None`

#### Raises

- If an error occurs while creating the directory.

#### Example

```python
create_images_folder("/path/to/images")
```

## Logging

This module uses the `logging` module to log events at the INFO level. The logging configuration is set up using `logging.basicConfig(level=logging.INFO)`.

### Author

- Dmitrii Pivnev (sibdip)