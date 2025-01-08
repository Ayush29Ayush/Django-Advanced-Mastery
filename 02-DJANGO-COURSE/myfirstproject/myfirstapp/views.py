from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    # return JsonResponse({"message": "Hello, Django!"})
    # return HttpResponse("Hello, Django!")
    return render(request, "index.html")


def contact(request):
    print(request.GET)
    # print("Hello, This is Contact Page!!!")
    # print("If we add 2 + 3, we get", 2 + 3)
    # return HttpResponse("Hello, This is Contact Page!")
    return render(request, "contact.html")


def dynamic_route(request, number):
    for i in range(0, 10):
        print(f"{number} * {i+1} = ", (i + 1) * number)
    return HttpResponse(f"Hello, the number is {number}")
