from celery import shared_task
import time
import os
import requests
from faker import Faker
import random
import time
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from home.models import UserInfo

fake = Faker()


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
    
    
@shared_task
def create_user_info():
    name = fake.name()
    email = fake.email()
    password = fake.password()
    age = random.randint(10, 30)  
    
    gender_choices = ['M', 'F', 'O', 'P']
    gender = random.choice(gender_choices)
    
    user_info = UserInfo.objects.create(name=name,email=email,password=password,age=age,gender=gender)
    
    return f"User Info created with ID: {user_info.id}"


# You can choose between a specific set of periods:
# IntervalSchedule.DAYS
# IntervalSchedule.HOURS
# IntervalSchedule.MINUTES
# IntervalSchedule.SECONDS
# IntervalSchedule.MICROSECONDS
schedule, created = IntervalSchedule.objects.get_or_create(
    every=1,
    period=IntervalSchedule.MINUTES
)
# # That’s all the fields you need to create a scheduler: a period type and the frequency.

PeriodicTask.objects.update_or_create(
    interval = schedule,
    name = "Create UserInfo",
    task = "home.tasks.create_user_info",
)