[1mdiff --git a/api_script.py b/api_script.py[m
[1mindex e80b79c..ee74627 100644[m
[1m--- a/api_script.py[m
[1m+++ b/api_script.py[m
[36m@@ -4,6 +4,9 @@[m [mfrom datetime import date[m
 import requests[m
 from dotenv import load_dotenv[m
 [m
[32m+[m[32mdef is_image(media_type: str) -> bool:[m
[32m+[m[32m    return media_type == 'image'[m
[32m+[m
 load_dotenv()[m
 [m
 # APOD - Astronomy Picture of the Day [m
[36m@@ -19,10 +22,18 @@[m [mif not os.path.exists(images_folder):[m
 [m
 params = {[m
     "api_key": api_key,[m
[31m-    #"date": f"{today.year}-{today.month}-{today.day}"[m
[31m-    "date": "2022-01-1"[m
[32m+[m[32m    "date": f"{today.year}-{today.month}-{today.day}"[m
[32m+[m[32m    #"date": "2022-01-1"[m
     }[m
 [m
 response = requests.get(apod_url, params=params)[m
 [m
 print(response.text)[m
[32m+[m
[32m+[m[32mif response.status_code == 200:[m
[32m+[m[32m    if is_image(response.json()['media_type']):[m
[32m+[m[32m        hd_image_url = response.json()["hdurl"][m
[32m+[m[32m        print(hd_image_url)[m
[32m+[m
[32m+[m[32melse:[m
[32m+[m[32m    print(f"Operation failed. Status code: {response.status_code}.\n Probobly its too early in USA.")[m
