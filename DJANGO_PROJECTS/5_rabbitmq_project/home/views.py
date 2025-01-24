from django.http import JsonResponse
import random
from home.rabbitmq_producer import publish_message
from faker import Faker


fake = Faker()


def index(request):
    message = f"This is a demo message - {random.randint(0 , 100)}"
    names = [{"name": fake.name(), "address": fake.address()} for _ in range(10)]
    
    data_to_send = {
        "message": message,
        "names": names
    }

    publish_message(data=data_to_send)
    return JsonResponse({"message": message, "names": names})
