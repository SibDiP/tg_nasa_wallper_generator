import os
import logging

logging.basicConfig(level=logging.INFO)

def create_images_folder(dir: str) -> None:
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
            logging.info(f"Created {dir} folder.")
        except:
            logging.error(f"Error creating {dir} folder.")

if __name__ == "__main__":
    main()