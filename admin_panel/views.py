from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages 
from freelancer.models import Feedback
from django.core.paginator import Paginator
from django.db.models import Q


from .models import Activity, User, JobPosting, Payment, SystemHealth

# Admin dashboard view
def admin_dashboard(request):
    # Fetch recent activities
    recent_activity = Activity.objects.all().order_by('-timestamp')[:5]
    
    # Fetch counts for various sections
    total_users = User.objects.count()
    total_jobs = JobPosting.objects.count()
    total_payments = Payment.objects.count()
    try:
        system_health = SystemHealth.objects.get(id=1)  # Example query
    except SystemHealth.DoesNotExist:
        system_health = None
    
    # Render the admin dashboard template with context
    context = {
        'recent_activity': recent_activity,
        'total_users': total_users,
        'total_jobs': total_jobs,
        'total_payments': total_payments,
        'system_health': system_health,
    }
    
    return render(request, 'admin_panel/dashboard.html', context)

# View for managing users
def admin_manage_users(request):
    users = User.objects.all()
    return render(request, 'admin_panel/admin_manage_users.html', {'users': users})

def add_user(request):
    # Your logic to handle adding a user
    return render(request, 'admin_panel/add_user.html')
def view_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'admin_panel/view_user.html', {'user': user})
def edit_user(request, user_id):
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
        return redirect('admin_manage_users')  # Adjust the URL name as needed

    # Render the edit user template with the user data
    return render(request, 'admin_panel/edit_user.html', {'user': user})
def toggle_user_status(request, user_id):
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
    return redirect('admin_manage_users')  # Adjust the URL name as needed
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully.")  # Optional
        return redirect('admin_manage_users')  # Redirect to user management page
    return redirect('admin_manage_users')  # Fallback in case of a GET request
# Job Postings Overview


def job_postings(request):
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    status_filter = request.GET.get('status', '')

    jobs = JobPosting.objects.all()

    # Apply search and filters
    if search_query:
        jobs = jobs.filter(title__icontains=search_query)
    if category_filter:
        jobs = jobs.filter(category=category_filter)
    if status_filter:
        jobs = jobs.filter(status=status_filter)

    # Add pagination
    paginator = Paginator(jobs, 10)  # 10 jobs per page
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)

    return render(request, 'admin_panel/job_postings.html', {'jobs': jobs})

def add_job(request):
    if request.method == 'POST':
        # Get the form data from the request
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        budget = request.POST.get('budget')
        status = request.POST.get('status')

        # Create a new JobPosting object
        job_posting = JobPosting(
            title=title,
            category=category,
            description=description,
            budget=budget,
            status=status
        )

        # Save the new JobPosting object to the database
        job_posting.save()

        # Redirect to a success page (or any other page you prefer)
        return redirect('job_postings')

    return render(request, 'admin_panel/add_job.html')
# View job
def view_job(request, job_id):
    # Get the job object or return a 404 if it doesn't exist
    job = get_object_or_404(JobPosting, id=job_id)
    
    # Render the view with the job data
    return render(request, 'admin_panel/view_job.html', {'job': job})

# Edit job
def edit_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    
    # If the form is submitted (POST request)
    if request.method == 'POST':
        # Update the job fields from the form data
        job.title = request.POST.get('title')
        job.category = request.POST.get('category')
        job.description = request.POST.get('description')
        job.budget = request.POST.get('budget')
        job.status = request.POST.get('status')
        
        job.save()  # Save the changes to the database
        return redirect('job_postings')  # Redirect to the job postings list after editing
    
    # If it's a GET request, just render the edit form with the current job data
    return render(request, 'admin_panel/edit_job.html', {'job': job})

# Delete job
def delete_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    
    if request.method == 'POST':
        job.delete()  # Delete the job from the database
        return redirect('job_postings')  # Redirect to the job postings list
    
    # Render a confirmation page to ask if the user is sure
    return render(request, 'admin_panel/delete_job.html', {'job': job})
# Payment Management
def payment_management(request):
    return render(request, 'payment_management.html')

# System Activity
def system_activity(request):
    return render(request, 'system_activity.html')

# Analytics
def analytics(request):
    return render(request, 'analytics.html')

# Notifications
def notifications(request):
    return render(request, 'notifications.html')

# Support Tickets
def support_tickets(request):
    return render(request, 'support_tickets.html')

# User Feedback
def user_feedback(request):
    return render(request, 'user_feedback.html')

# Manage Freelancers
def manage_freelancers(request):
    return render(request, 'manage_freelancers.html')

# Manage Clients
def manage_clients(request):
    return render(request, 'manage_clients.html')

# System Health
def system_health(request):
    return render(request, 'system_health.html')

# New Registrations
def new_registrations(request):
    return render(request, 'new_registrations.html')