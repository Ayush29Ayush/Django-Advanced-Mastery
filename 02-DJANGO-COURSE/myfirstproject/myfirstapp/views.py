from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from myfirstapp.forms import DjangoStudentForm, DjangoModelStudentForm
from myfirstapp.models import Student2


# Create your views here.
def index(request):
    # return JsonResponse({"message": "Hello, Django!"})
    # return HttpResponse("Hello, Django!")
    return render(request, "index.html")


def contact(request):
    # print(request.GET)
    # print("Hello, This is Contact Page!!!")
    # print("If we add 2 + 3, we get", 2 + 3)
    # return HttpResponse("Hello, This is Contact Page!")
    return render(request, "contact.html")


def dynamic_route(request, number):
    for i in range(0, 10):
        print(f"{number} * {i+1} = ", (i + 1) * number)
    return HttpResponse(f"Hello, the number is {number}")


def my_django_forms(request):
    # form = DjangoStudentForm(request.POST or None)
    form = DjangoStudentForm()
    context = {"form": form}
    print(request.method)
    if request.method == "GET":
        print("This is GET Request")
        print(request.GET)

    if request.method == "POST":
        print("This is POST Request")
        print(request.POST)

        data = DjangoStudentForm(request.POST)
        if data.is_valid():
            print("The cleaned form data is ", data.cleaned_data)
            name = data.cleaned_data.get("name")
            age = data.cleaned_data.get("age")
            Student2.objects.create(name=name, age=age)
            print("Data is valid and saved successfully in database...")
            return redirect("index")
        else:
            print(data.errors)

    return render(request, "my_django_forms.html", context=context)


def my_django_model_forms(request):
    # form = DjangoModelStudentForm(request.POST or None)
    form = DjangoModelStudentForm()
    context = {"form": form}
    print(request.method)
    if request.method == "GET":
        print("This is GET Request")
        print(request.GET)

    if request.method == "POST":
        print("This is POST Request")
        print(request.POST)

        data = DjangoModelStudentForm(request.POST)
        if data.is_valid():
            print("The cleaned form data is ", data.cleaned_data)
            data.save()
            print("Data is valid and saved successfully in database...")
            return redirect("index")
        else:
            print(data.errors)

    return render(request, "my_django_model_forms.html", context=context)

def my_html_forms(request):
    context = {}
    if request.method == "POST":
        print("This is POST Request")
        print(request.POST)
        print(request.FILES)
        name = request.POST.get("full_name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        upload_file = request.FILES.get("upload_file")
        
        Student2.objects.create(name=name, age=age, gender=gender, upload_file=upload_file)
        print("Data is valid and saved successfully in database...")
        return redirect("index")
        
    return render(request, "my_html_forms.html", context=context)