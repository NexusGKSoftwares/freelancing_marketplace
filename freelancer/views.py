from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Freelancer, Job, Notification, Feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import login 

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CustomUser 
from django.contrib import messages
from django.contrib.auth.models import User
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'freelancer/index.html')
    else:
        return HttpResponseRedirect(reverse('freelancer_dashboard'))
    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request, user)  # Auto-login after register
            messages.success(request, "register successful! You are now logged in.")
            return redirect('index')  # Redirect to the home page or desired page after successful register
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return redirect('register')

    # If GET request, render the register page
    return render(request, 'freelancer/register.html')
def login(request):
    if request.method == 'POST':
        # Get username and password from POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if user exists
        user = authenticate(username=username, password=password)

        
        if user is not None:
            # Log the user in if authentication is successful
            login(request, user)
            return redirect('dashboard')  # Replace with the name of your desired redirect page
        else:
            # If authentication fails, add an error message
            messages.error(request, "Invalid username or password.")
    
    # Render the login page if the method is GET or after an unsuccessful login attempt
    return render(request, 'freelancer/login.html')
# Dashboard view
@login_required
def dashboard(request):
    if request.user.role == 'freelancer':
        return redirect('freelancer_dashboard')
    elif request.user.role == 'client':
        return redirect('client_dashboard')
    elif request.user.role == 'admin':
        return redirect('admin_dashboard')
    else:
        return HttpResponse("Role not recognized. Please contact support.")

# Placeholder views for different dashboards
@login_required
def freelancer_dashboard(request):
    return HttpResponse("Welcome to the Freelancer Dashboard!")

@login_required
def client_dashboard(request):
    return HttpResponse("Welcome to the Client Dashboard!")

@login_required
def admin_dashboard(request):
    return HttpResponse("Welcome to the Admin Dashboard!")
@login_required
def freelancer_dashboard(request):
    
    # Assuming the user is logged in
    freelancer = Freelancer.objects.get(user=request.user)  # Use related 'user' field here
    available_jobs_count = Job.objects.filter(is_available=True).count()
    notifications = Notification.objects.filter(freelancer=freelancer)
    
    # Calculate earnings and pass the data for the chart
    earnings_data = [100, 200, 300, 400]  # Example earnings data
    earnings_labels = ['January', 'February', 'March', 'April']  # Example labels for earnings

    return render(request, 'dashboard.html', {
        'freelancer': freelancer,
        'available_jobs_count': available_jobs_count,
        'notifications': notifications,
        'earnings_data': earnings_data,
        'earnings_labels': earnings_labels,
    })

@login_required
def freelancer_edit_profile(request):
    # Handle the profile editing logic
    return render(request, 'freelancer_edit_profile.html')

@login_required
def freelancer_payment_overview(request):
    freelancer = Freelancer.objects.get(user=request.user)
    # Fetch freelancer payments
    return render(request, 'freelancer_payment_overview.html', {'freelancer': freelancer})

@login_required
def freelancer_ongoing_jobs(request):
    freelancer = Freelancer.objects.get(user=request.user)
    ongoing_jobs = freelancer.jobs.filter(status='ongoing')
    return render(request, 'freelancer_ongoing_jobs.html', {'ongoing_jobs': ongoing_jobs})

@login_required
def freelancer_available_jobs(request):
    available_jobs = Job.objects.filter(status='available')
    return render(request, 'freelancer_available_jobs.html', {'available_jobs': available_jobs})

@login_required
def freelancer_notifications(request):
    freelancer = Freelancer.objects.get(user=request.user)
    notifications = Notification.objects.filter(freelancer=freelancer)
    return render(request, 'freelancer_notifications.html', {'notifications': notifications})

@login_required
def freelancer_feedback(request):
    freelancer = Freelancer.objects.get(user=request.user)
    feedbacks = freelancer.feedbacks.all()
    return render(request, 'freelancer_feedback.html', {'feedbacks': feedbacks})

@login_required
def freelancer_job_details(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'freelancer_job_details.html', {'job': job})

@login_required
def freelancer_payment_history(request):
    freelancer = Freelancer.objects.get(user=request.user)
    # Fetch payment history
    return render(request, 'freelancer_payment_history.html', {'freelancer': freelancer})

@login_required
def freelancer_job_history(request):
    freelancer = Freelancer.objects.get(user=request.user)
    completed_jobs = freelancer.jobs.filter(status='completed')
    return render(request, 'freelancer_job_history.html', {'completed_jobs': completed_jobs})
