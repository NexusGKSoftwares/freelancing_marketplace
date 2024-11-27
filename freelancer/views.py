from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect(reverse('Portal:home'))
    
def freelancer_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Registration successful! Please login.")
                return redirect('freelancer_login')
        else:
            messages.error(request, "Passwords do not match!")
    return render(request, 'freelancer/register.html')

def freelancer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('freelancer_dashboard')
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, 'freelancer/login.html')

def freelancer_logout(request):
    logout(request)
    return redirect('freelancer_login')


@login_required
def dashboard(request):
    return render(request, 'freelancer/dashboard.html')
