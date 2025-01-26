from django.urls import path
from home.consumer import MainConsumer

websocket_urlpatterns = [
    path("ws/main/", MainConsumer.as_asgi()),
]

# from django.urls import re_path
# from home.consumer import ChatConsumer

# websocket_urlpatterns = [
#     re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
# ]