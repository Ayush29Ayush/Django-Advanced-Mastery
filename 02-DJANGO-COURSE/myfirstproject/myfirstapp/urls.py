from django.urls import path
from myfirstapp.views import index, contact, dynamic_route

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("dynamic_route/<int:number>", dynamic_route, name="dynamic_route"),
]
