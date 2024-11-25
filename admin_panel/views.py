from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.hashers import check_password
from django.contrib import messages

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Query the database for the admin user
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, password FROM admins WHERE username = %s", [username])
            admin = cursor.fetchone()

        # Validate the user and password
        if admin and check_password(password, admin[1]):
            # Store admin session
            request.session['admin_id'] = admin[0]
            return redirect("/admin_panel/dashboard/")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "admin_panel/login.html")


def dashboard(request):
    # Ensure admin is logged in
    if 'admin_id' not in request.session:
        return redirect('/admin_panel/login/')
    return render(request, 'admin_panel/dashboard.html')
