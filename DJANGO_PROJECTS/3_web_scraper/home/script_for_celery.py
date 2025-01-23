import requests
from bs4 import BeautifulSoup
from home.models import News
import os
import re
import uuid
from django.conf import settings
from home.tasks import download_image

def scrape_imdb_news():
    url = "https://www.imdb.com/news/movie/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    news_items = soup.find_all("div", class_="ipc-list-card--border-line")
    for item in news_items:
        # Use a regular expression to match any class starting with 'ipc-link ipc-link--base'
        title_tag = item.find("a", class_=re.compile("ipc-link ipc-link--base"))
        description = item.find("div", class_="ipc-html-content-inner-div")
        image_tag = item.find("img", class_="ipc-image")  # Get the image tag
        
        image_path = None
        if image_tag:
            image_url = image_tag["src"]  # Extract the image URL from the 'src' attribute
            image_name = f"image_{uuid.uuid4()}.jpg"
            folder_path = os.path.join(settings.MEDIA_ROOT, 'imdb_images_downloads')  # Folder to store images

            # Asynchronously download the image with Celery
            image_task = download_image.delay(image_url=image_url, folder_path=folder_path, image_name=image_name)

            image_field_value = image_url
        else:
            image_field_value = None

        if title_tag:
            title = title_tag.text.strip() if title_tag else "No title"
            external_link = title_tag["href"]
        else:
            title = "No title"
            external_link = None

        description = description.text.strip() if description else "No description"

        # Save the initial news item with the original image URL (not the image path)
        news = {
            "title": title,
            "description": description,
            "image": image_field_value,  # Storing the original image URL
            "external_link": external_link,
        }

        news_instance = News.objects.create(**news)

        # Once the image is downloaded, update the image_path field in the database
        if image_task:
            # You can now track the completion of the task (you can also add some retry logic if needed)
            image_path = image_task.get()  # Get the result from the task (the path of the saved image)
            
            # After the image is downloaded, update the `image_path` in the model
            if image_path:
                news_instance.image_path = os.path.join('imdb_images_downloads', os.path.basename(image_path))
                news_instance.save()  # Save the updated model

