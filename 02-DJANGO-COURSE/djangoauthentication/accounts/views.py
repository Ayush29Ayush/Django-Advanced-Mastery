import email
from email import message
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from accounts.emailer import sendOtpToEmail
import random
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

User = get_user_model()


def login_page(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        user_obj = User.objects.filter(phone_number=phone_number)
        if not user_obj.exists():
            return redirect("/")

        email = user_obj[0].email
        otp = random.randint(1000, 9999)
        user_obj.update(otp=otp)
        user_obj[0].save()
        subject = "OTP for Login"
        message = f"Your OTP is {otp}"
        sendOtpToEmail(email=email, subject=subject, message=message)
        return redirect(f"/check-otp/{user_obj[0].id}/")

    return render(request, "login.html")


def check_otp(request, user_id):
    if request.method == "POST":
        otp = request.POST.get("otp")
        user_obj = User.objects.get(id=user_id)
        if user_obj.otp == int(otp):
            messages.success(request, "OTP verified successfully")
            login(request, user_obj)
            return redirect("/dashboard/")
        else:
            messages.error(request, "Invalid OTP")
            return redirect("/check-otp/")

    return render(request, "check-otp.html")


@login_required(login_url="/")
def dashboard(request):
    return HttpResponse("You are logged in")
