from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, "You have successfully registered!")
        return redirect("usermodule:login")
    return render(request, "users/register.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("bookmodule:list_books")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "users/login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("usermodule:login")
