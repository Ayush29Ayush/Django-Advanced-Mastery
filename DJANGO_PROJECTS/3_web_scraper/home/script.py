import requests
from bs4 import BeautifulSoup
from home.models import News
import os
import re
import uuid
from django.conf import settings

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
            folder_path = os.path.join(settings.MEDIA_ROOT, 'imdb_images_downloads') # Use MEDIA_ROOT to save images under the 'media/imdb_images_downloads' folder
            image_path = download_image(image_url=image_url,folder_path=folder_path,image_name=image_name)
            print(f"Downloaded image: {image_path}")
            image_field_value = image_url
            image_path_field_value = os.path.join('imdb_images_downloads', os.path.basename(image_path)) if image_path else None
        else:
            image_field_value = None
            image_path_field_value = None

        if title_tag:
            title = title_tag.text.strip() if title_tag else "No title"
            external_link = title_tag["href"]
        else:
            title = "No title"
            external_link = None

        description = description.text.strip() if description else "No description"
        
        news = {
            "title": title,
            "description": description,
            "image": image_field_value,
            "image_path": image_path_field_value,
            "external_link": external_link,
        }

        News.objects.create(**news)