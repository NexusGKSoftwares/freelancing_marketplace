from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Freelancer, Job, Notification, Feedback, Payment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import login 

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.models import User
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'freelancer/index.html')
    else:
        return HttpResponseRedirect(reverse('freelancer_dashboard'))
    
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('freelancer_dashboard')  # Adjust this as per your application logic
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('register')

    return render(request, 'freelancer/register.html')
def freelancer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login the user
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect('freelancer_dashboard')  # Redirect to home or any page after login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  # Stay on login page for retry
    
    return render(request, 'freelancer/login.html')  # Render the login page if GET request
@login_required
def freelancer_dashboard(request):
    # Get the current user
    user = request.user

    # Fetch freelancer profile data
    try:
            freelancer = request.user.freelancer_profile
    except Freelancer.DoesNotExist:
            freelancer = Freelancer.objects.create(user=request.user)


    # Fetch active jobs, completed jobs, and available jobs
    active_jobs = freelancer.jobs.filter(status='Active')
    completed_jobs = freelancer.jobs.filter(status='Completed')
    available_jobs_count = Job.objects.filter(status='Available').count()

    # Fetch notifications for the freelancer
    notifications = Notification.objects.filter(user=user).order_by('-created_at')

    # Fetch feedback related to the freelancer
    feedbacks = Feedback.objects.filter(freelancer=freelancer).order_by('-date')

    # Context to pass to the template
    context = {
        'user': user,
        'freelancer': {
            'total_earnings': freelancer.total_earnings,
            'active_jobs': active_jobs,
            'jobs': freelancer.jobs.all(),
            'completed_jobs': completed_jobs,
            'feedbacks': feedbacks,
        },
        'notifications': notifications,
        'available_jobs_count': available_jobs_count,
    }

    return render(request, 'freelancer/dashboard.html', context)


@login_required
def freelancer_edit_profile(request):
    # Handle the profile editing logic
    return render(request, 'freelancer_edit_profile.html')

@login_required
def freelancer_payment_overview(request):
    # Assuming the logged-in user is associated with a freelancer profile
    freelancer = get_object_or_404(Freelancer, user=request.user)
    payments = Payment.objects.filter(freelancer=freelancer).order_by('-date')

    context = {
        'freelancer': freelancer,
        'payments': payments,
    }

    return render(request, 'freelancer/freelancer_payment_overview.html', context)

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
