from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/admin_panel/dashboard/")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "admin/login.html")

def dashboard(request):
    # Logic for rendering the dashboard
    return render(request, 'admin_panel/dashboard.html')