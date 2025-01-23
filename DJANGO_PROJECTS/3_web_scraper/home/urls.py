
from django.urls import path
from home.views import index, run_scraper, celery_task_testing

urlpatterns = [
    path('', index, name="index"),
    path('run-scraper/', run_scraper, name="run_scraper"),
    path('celery-task-testing/', celery_task_testing, name="celery_task_testing")
]