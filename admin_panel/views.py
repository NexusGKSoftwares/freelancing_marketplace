from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Admin users must be marked as staff
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, 'admin_panel/login.html')
