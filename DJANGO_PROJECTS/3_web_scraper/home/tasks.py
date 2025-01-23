from celery import shared_task
import time
import os
import requests


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y

@shared_task
def download_image(image_url, folder_path, image_name):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    image_path = os.path.join(folder_path, image_name)

    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        return image_path
    else:
        return None