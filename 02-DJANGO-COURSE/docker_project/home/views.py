from django.http import JsonResponse


def index(request):
    json_data = {"status": "success", "message": "Hello, Docker is up and running!"}
    return JsonResponse(json_data, status=200)