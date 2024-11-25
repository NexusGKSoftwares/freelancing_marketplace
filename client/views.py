from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def client_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff is False:  # To distinguish from admin users
            login(request, user)
            return redirect('client_dashboard')
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, 'client/login.html')

@login_required
def dashboard(request):
    return render(request, 'client/dashboard.html')

def client_logout(request):
    logout(request)
    return redirect('client_login')