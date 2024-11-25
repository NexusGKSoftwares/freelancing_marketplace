from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.db import connection

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Fetch admin user from the database
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, password FROM admins WHERE username = %s", [username])
            admin = cursor.fetchone()

        if admin and check_password(password, admin[1]):
            # Login successful
            request.session['admin_id'] = admin[0]
            return redirect('admin_dashboard')  # Adjust to your admin dashboard URL

        # Login failed
        return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'admin_panel/dashboard.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')