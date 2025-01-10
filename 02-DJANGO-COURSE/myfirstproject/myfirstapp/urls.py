from django.urls import path
from myfirstapp.views import index, contact, dynamic_route, my_django_forms, my_django_model_forms ,my_html_forms

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("dynamic_route/<int:number>", dynamic_route, name="dynamic_route"),
    path("my_django_forms/", my_django_forms, name="my_django_forms"),
    path("my_django_model_forms/", my_django_model_forms, name="my_django_model_forms"),
    path("my_html_forms/", my_html_forms, name="my_html_forms"),
]
