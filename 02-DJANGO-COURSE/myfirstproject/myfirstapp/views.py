from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from myfirstapp.forms import DjangoStudentForm, DjangoModelStudentForm
from myfirstapp.models import Skills, Student, Student2
from django.db.models import Q
from myfirstapp.utils import bulk_delete_brands, bulk_create_brands, bulk_update_brands


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

        Student2.objects.create(
            name=name, age=age, gender=gender, upload_file=upload_file
        )
        print("Data is valid and saved successfully in database...")
        return redirect("index")

    return render(request, "my_html_forms.html", context=context)


def search_page(request):
    students = Student.objects.all()

    search = request.GET.get("search", "")
    age = request.GET.get("age", "")
    if search:
        students = students.filter(
            Q(name__icontains=search)
            | Q(mobile_number__icontains=search)
            | Q(email__icontains=search)
            | Q(gender__icontains=search)
            | Q(student_bio__icontains=search)
        )

    skills = Skills.objects.filter()
    if age:
        if age == "1":
            students = students.filter(age__gte=18, age__lte=20).order_by("age")
        if age == "2":
            students = students.filter(age__gte=20, age__lte=22).order_by("age")
        if age == "3":
            students = students.filter(age__gte=22, age__lte=24).order_by("age")

    context = {"students": students, "search": search}
    return render(request, "search.html", context)


def bulk_operations_view(request):
    bulk_operation = request.GET.get("bulk_operation", "")
    num_entries = int(request.GET.get("num_entries", 10))  # Default to 10 entries
    message = ""
    error = ""

    if bulk_operation:
        if bulk_operation == "create":
            print("Creating", num_entries, "brands...")
            message = bulk_create_brands(num_entries)
        elif bulk_operation == "update":
            print("Updating", num_entries, "brands...")
            message = bulk_update_brands(num_entries)
        elif bulk_operation == "delete":
            print("Deleting", num_entries, "brands...")
            message = bulk_delete_brands(num_entries)
        else:
            error = "Invalid bulk operation type."
    else:
        error = "No bulk operation specified."

    return render(request, "bulk_operations.html", {"message": message, "error": error})
