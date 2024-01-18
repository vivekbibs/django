from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # login(request, user)
            # Redirect to a success page.
            return render(request, "login/success.html")
    
        else:
            return render(request, "login/error.html")
    else:
        return render(request, "login/login.html")
