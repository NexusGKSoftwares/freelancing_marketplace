from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserProfileForm  # Form to handle profile update
from django.db.models import Q  # For complex search queries

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'freelancer/index.html')
    else:
        return HttpResponseRedirect(reverse('freelancer_dashboard'))
    
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
                messages.success(request, "Registration successful! Please log in.")
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


# Profile Page View
@login_required
def profile(request):
    # Get the current logged-in user
    user = request.user
    # Get the user profile related to the logged-in user
    user_profile = user.profile
    
    return render(request, 'freelancer/profile.html', {'user': user, 'user_profile': user_profile})

# Edit Profile View
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()  # Save the updated profile information
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')  # Redirect to profile page
    else:
        form = UserProfileForm(instance=request.user.profile)

    return render(request, 'freelancer/edit_profile.html', {'form': form})

# Search Users View
def profile_search(request):
    search_query = request.GET.get('search', '')
    search_results = []

    if search_query:
        # Searching across username, email, location, phone number, and skills
        search_results = User.objects.filter(
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(profile__location__icontains=search_query) |
            Q(profile__phone_number__icontains=search_query) |
            Q(profile__skills__icontains=search_query)  # Assuming 'skills' is a field in UserProfile
        )

    return render(request, 'freelancer/profile_search_results.html', {
        'search_results': search_results,
        'search_query': search_query  # Pass search query to keep in search box
    })

