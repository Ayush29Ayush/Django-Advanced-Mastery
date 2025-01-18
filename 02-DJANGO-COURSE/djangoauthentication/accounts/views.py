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
from django.core.cache import cache

User = get_user_model()


def login_page(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        if cache.get(phone_number):
            data = cache.get(phone_number)
            print(data)
            data["count"] += 1
            if data["count"] >= 3:
                cache.set(phone_number, data, 60 * 5)
                messages.error(request, "You can request OTP after 5 mins.")
                return redirect("/")

            cache.set(phone_number, data, 60 * 1)

        if not cache.get(phone_number):
            data = {"phone_number": phone_number, "count": 1}
            cache.set(phone_number, data, 60 * 1)

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
        if cache.get(user_obj.phone_number):
            data = cache.get(user_obj.phone_number)
            if data['count'] >= 3:
                messages.error(request, "You can request OTP after 5 mins.")
                return redirect('/') 
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
