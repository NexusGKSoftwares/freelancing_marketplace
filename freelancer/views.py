from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Freelancer, Job, Notification, Feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CustomUser 
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'freelancer/index.html')
    else:
        return HttpResponseRedirect(reverse('freelancer_dashboard'))
    
# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Set user role from the form
            user_role = request.POST.get('role')
            if user_role in ['freelancer', 'client', 'admin']:
                user.role = user_role
            user.save()
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'freelancer/register.html', {'form': form})

# Login view
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            return render(request, 'freelancer/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'freelancer/login.html', {'form': form})

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
