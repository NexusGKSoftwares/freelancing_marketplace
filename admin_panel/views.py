from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:  # Check if the user exists
            login(request, user)  # Log the user in
            return redirect('/admin_panel/dashboard/')  # Redirect to admin dashboard
        else:
            # Display error message if authentication fails
            messages.error(request, "Invalid username or password")
    
    return render(request, 'admin/login.html')
