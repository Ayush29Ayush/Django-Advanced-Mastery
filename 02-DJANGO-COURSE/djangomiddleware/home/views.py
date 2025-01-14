from django.shortcuts import render
from django.http import JsonResponse
from home.models import Store


# Create your views here.
def index(request):

    store = Store.objects.get(bmp_id=request.headers.get("bmp_id"))

    headers = dict(request.headers)
    data = {
        "status": "success",
        "message": "Hello, Django!",
        "headers": headers,
        "store": {"bmp_id": store.bmp_id, "store_name": store.store_name},
    }
    return JsonResponse(data)
