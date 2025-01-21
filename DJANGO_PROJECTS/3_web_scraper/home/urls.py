
from django.urls import path
from home.views import index, run_scraper

urlpatterns = [
    path('', index, name="index"),
    path('run-scraper/', run_scraper, name="run_scraper")
]