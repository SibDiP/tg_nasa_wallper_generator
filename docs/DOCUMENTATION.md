# **NASA APOD API Downloader**

## Description

This script allows to download images from the NASA APOD (Astronomy Picture of the Day) API.

## Usage

Add your NASA api_key to 'example.env' and rename it to '.env'.

## Functions

### download_apod_image(target_date: date = None) -> None

Downloads an image from the NASA APOD API to IMAGES_OUTPUT_DIR.

- `date`: The date of the target image in date format. Take yesterday by defoult because of the timezone difference issues (it can be yesterday in USA timezone).

### Constants
Stored in .env.

- `API_KEY`: Default NASA APOD API key.
- `API_URL`: URL of the NASA APOD API.
- `IMAGES_OUTPUT_DIR`: Directory for saved photos. './photos' by defoult.

# **Image Cropper Documentation**

## Overview

The `image_cropper.py` script is a utility for cropping images to a 9:16 aspect ratio. It takes an input image file and saves the cropped image to a specified output path.

## Usage

To use the `image_cropper.py` script, simply call the `crop_image` function and pass in the input image path and output path as arguments.

## Function

### `crop_image(image_path: str, output_path: str) -> None`

Crops the given image to a 9:16 aspect ratio and saves it to the output path.

#### Args

- `image_path`: The path to the image to be cropped.
- `output_path`: The path where the cropped image will be saved.

#### Returns

- `None`

#### Raises

- `FileNotFoundError`: If the input image file or output file path is not found.

## How it Works

1. The script opens the input image file using PIL.
2. It calculates the new width and height of the image based on the 9:16 aspect ratio.
3. It calculates the crop box coordinates to center the image within the new dimensions.
4. It crops the image using the calculated crop box coordinates.
5. It saves the cropped image to the specified output path.

## Logging

The script uses the `logging` module to log information and error messages. The logging level is set to `INFO` by default.

## Example Usage

```python
from image_cropper import crop_image

input_image_path = 'input_image.jpg'
output_image_path = 'output_image.jpg'

crop_image(input_image_path, output_image_path)
```

This will crop the `input_image.jpg` file to a 9:16 aspect ratio and save the cropped image to `output_image.jpg`.


# utils.py


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