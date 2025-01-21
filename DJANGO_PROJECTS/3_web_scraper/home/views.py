from django.shortcuts import render
from home.script import scrape_imdb_news
from home.models import News
from django.http import JsonResponse


# Create your views here.
def run_scraper(request):
    scrape_imdb_news()
    return JsonResponse({"status": True, "message": "Scraper executed successfully."})

def index(request):
    context = {
        "news_data": News.objects.all()
    }
    return render(request, "index.html", context=context)