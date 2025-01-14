from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
    data = {"status": "success", "message": "Hello, Django!"}
    return JsonResponse(data)
