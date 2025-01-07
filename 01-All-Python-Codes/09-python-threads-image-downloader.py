import os
import requests
import uuid
import time
import threading


class ImageDownloaderByUrl:

    def __init__(self, url):
        self.url = url

    def run(self):
        image = requests.get(self.url).content
        image_name = f"{uuid.uuid4()}.jpg"
        download_folder = "09-python-threads-images_downloaded"

        #! Create the download folder if it doesn't exist
        os.makedirs(download_folder, exist_ok=True)

        with open(os.path.join(download_folder, image_name), "wb") as f:
            f.write(image)
            print(f"Downloaded {image_name} to {download_folder}")


if __name__ == "__main__":

    print(f"Thread name is {threading.current_thread().name} with id - {threading.get_ident()}")

    urls = [
        "https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        "https://images.pexels.com/photos/14661923/pexels-photo-14661923.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
    ]

    for url in urls:
        imageDownloader = ImageDownloaderByUrl(url=url)
        imageDownloader.run()

    print("---------------All downloads completed---------------")
