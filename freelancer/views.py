from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.timezone import now, timedelta
from django.db.models import F
from admin_panel.models import JobPosting, StaticPage
from .models import Freelancer, Job, Notification, Feedback, Payment, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import login 
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ProfilePictureForm 
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.db.models import Prefetch
from .models import Freelancer
from freelancer import models
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
    notifications = Notification.objects.filter(user=user).order_by('created_at')

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
def freelancer_edit_user(request, user_id):
    # Fetch the user by ID or return a 404 if not found
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        # Get data from the request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        is_active = request.POST.get('is_active') == 'True'

        # Update the user object
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.is_active = is_active

        # Save the updated user object
        user.save()

        # Add a success message (optional)
        messages.success(request, 'User details updated successfully.')

        # Redirect to the user management page
        return redirect('freelancer_profile')  # Adjust the URL name as needed

    # Render the edit user template with the user data
    return render(request, 'freelancer/edit_user.html', {'user': user})
def toggle_freelancer_status(request, user_id):
    # Fetch the user by ID or return a 404 if not found
    user = get_object_or_404(User, id=user_id)
    
    # Toggle the active status
    user.is_active = not user.is_active
    user.save()

    # Add a success message
    if user.is_active:
        messages.success(request, f"{user.username}'s account has been activated.")
    else:
        messages.success(request, f"{user.username}'s account has been suspended.")

    # Redirect back to the user management page or another relevant page
    return redirect('index')  # Adjust the URL name as needed
@login_required
def freelancer_profile(request):
    # Fetch the freelancer object
    freelancer = get_object_or_404(Freelancer, user=request.user)

    # Fetch jobs (update this based on the actual relationship)
    jobs = freelancer.jobs.all() if hasattr(freelancer, 'jobs') else None

    context = {
        'freelancer': freelancer,
        'jobs': jobs,  # Pass jobs to the template
    }
    return render(request, 'freelancer/freelancer_profile.html', context)
@login_required
def upload_profile_picture(request):
    # Ensure profile exists for the user
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            profile = request.user.profile
            profile.picture = form.cleaned_data['picture']
            profile.save()
            messages.success(request, "Profile picture updated successfully!")
            return redirect('freelancer_profile')
    else:
        form = ProfilePictureForm()

    return render(request, 'freelancer/upload_profile_picture.html', {'form': form})

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
    freelancer = get_object_or_404(Freelancer, user=request.user)
    ongoing_jobs = freelancer.jobs.filter(status='ongoing').order_by('deadline')
    
    # Add pagination
    paginator = Paginator(ongoing_jobs, 5)  # Show 5 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'freelancer/freelancer_ongoing_jobs.html', {'page_obj': page_obj})

@login_required
def freelancer_available_jobs(request):
    # Get query parameters for filtering and sorting
    category = request.GET.get('category', '')
    sort_order = request.GET.get('sort', '')

    # Base query for jobs with status "Open"
    jobs = JobPosting.objects.filter(status='Open')

    # Filter by category if provided
    if category:
        jobs = jobs.filter(category=category)

    # Sort by budget
    if sort_order == 'low':
        jobs = jobs.order_by('budget')
    elif sort_order == 'high':
        jobs = jobs.order_by('-budget')

    # Add a "New" flag for jobs posted within the last 7 days
    for job in jobs:
        job.is_new = (now() - timedelta(days=7)) <= job.created_at

    # Get distinct categories for filtering
    categories = JobPosting.objects.values_list('category', flat=True).distinct()

    return render(request, 'freelancer/freelancer_available_jobs.html', {
        'available_jobs': jobs,
        'categories': categories,
        'selected_category': category,
        'sort_order': sort_order,
    })

@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    # Logic to handle the application process (e.g., creating an application object)
    messages.success(request, f'You have successfully applied for the job: {job.title}')
    return redirect('freelancer/freelancer_available_jobs.html')

@login_required
def freelancer_notifications(request):
    freelancer = get_object_or_404(Freelancer, user=request.user)
    notifications = Notification.objects.filter(freelancer=freelancer).order_by('deadline')
    
    # Mark all notifications as read when visiting this view
    notifications.update(is_read=True)
    
    return render(request, 'freelancer/freelancer_notifications.html', {'notifications': notifications})


@login_required
def freelancer_feedback(request):
    freelancer = get_object_or_404(Freelancer, user=request.user)
    feedbacks = freelancer.feedbacks.all().order_by('-date_submitted')
    
    return render(request, 'freelancer/freelancer_feedback.html', {'feedbacks': feedbacks})


def freelancer_job_details(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    
    # Calculate the application percentage (if max_applicants is set)
    if job.max_applicants:
        application_percentage = (job.current_applicants / job.max_applicants) * 100
    else:
        application_percentage = 0  # If no max applicants, set it to 0%

    return render(request, 'freelancer/freelancer_job_details.html', {
        'job': job,
        'application_percentage': application_percentage,
    })

@login_required
def freelancer_payment_history(request):
    freelancer = get_object_or_404(Freelancer, user=request.user)
    payments = Payment.objects.filter(freelancer=freelancer).order_by('-payment_date')
    
    # Add pagination
    paginator = Paginator(payments, 5)  # Show 5 payments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'freelancer/freelancer_payment_history.html', {'page_obj': page_obj})


@login_required
def freelancer_job_history(request):
    freelancer = get_object_or_404(Freelancer, user=request.user)
    completed_jobs = freelancer.jobs.filter(status='completed').order_by('-completion_date')
    
    # Add pagination
    paginator = Paginator(completed_jobs, 5)  # Show 5 completed jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'freelancer/freelancer_job_history.html', {'page_obj': page_obj})

def get_static_page_content(request, page):
    static_page = get_object_or_404(StaticPage, page=page)
    return render(request, f"{page}.html", {"title": static_page.title, "content": static_page.content})

def about(request):
    return get_static_page_content(request, 'about')

def contact_us(request):
    return get_static_page_content(request, 'contact_us')

def features(request):
    return get_static_page_content(request, 'features')

def terms_and_conditions(request):
    return get_static_page_content(request, 'terms_and_conditions')

def privacy_policy(request):
    return get_static_page_content(request, 'privacy_policy')

def faq(request):
    return get_static_page_content(request, 'faq')
def logout_view(request):
    logout(request)
    return redirect('index')