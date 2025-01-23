from unittest import result
from django.shortcuts import render
# from home.script import scrape_imdb_news
from home.script_for_celery import scrape_imdb_news
from home.models import News
from django.http import JsonResponse
from home.tasks import add

# Create your views here.
def run_scraper(request):
    scrape_imdb_news()
    return JsonResponse({"status": True, "message": "Scraper executed successfully."})

def index(request):
    context = {
        "news_data": News.objects.all()
    }
    return render(request, "index.html", context=context)

def celery_task_testing(request):
    # result = add(2, 3) #! This will run the task synchronously
    # Call the Celery task asynchronously
    result = add.delay(2, 3)  #! This will run the task asynchronously using Celery

    # Return task details (task ID, status, and result once completed)
    response_data = {
        "task_id": result.id,
        "status": result.status,  # This shows the status of the task (e.g., 'PENDING', 'SUCCESS')
    }

    # If the task is done, add the result to the response
    if result.ready():  # Check if the task is finished
        response_data["result"] = result.result  # Add the task result

    return JsonResponse(response_data)