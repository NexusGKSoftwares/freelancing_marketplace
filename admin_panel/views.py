from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages 
from freelancer.models import Feedback
from .forms import UserEditForm


from .models import Activity, User, JobPosting, Payment, SystemHealth, SupportTicket 

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
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_manage_users')  # Redirect to user management page
    else:
        form = UserEditForm(instance=user)
    return render(request, 'admin_panel/edit_user.html', {'form': form, 'user': user})
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully.")  # Optional
        return redirect('admin_manage_users')  # Redirect to user management page
    return redirect('admin_manage_users')  # Fallback in case of a GET request
# View for managing job postings
def admin_job_postings(request):
    job_postings = JobPosting.objects.all()
    return render(request, 'admin_panel/admin_job_postings.html', {'job_postings': job_postings})

# View for managing payments
def admin_payments(request):
    payments = Payment.objects.all()
    return render(request, 'admin_panel/admin_payments.html', {'payments': payments})

# View for system activity
def admin_system_activity(request):
    activities = Activity.objects.all()
    return render(request, 'admin_panel/admin_system_activity.html', {'activities': activities})

# View for viewing platform analytics
def admin_analytics(request):
    # Example placeholder for analytics data (replace with actual data)
    analytics_data = {
        'traffic': 5000,
        'growth': 15,
        'user_engagement': 80,
    }
    return render(request, 'admin_panel/admin_analytics.html', {'analytics_data': analytics_data})

# View for managing notifications
def admin_notifications(request):
    # Example placeholder for notifications
    notifications = [
        {'message': 'New user registered.', 'timestamp': '2024-12-01 12:30'},
        {'message': 'Payment received for job 101.', 'timestamp': '2024-12-01 14:00'},
    ]
    return render(request, 'admin_panel/admin_notifications.html', {'notifications': notifications})

# View for managing support tickets
def admin_support_tickets(request):
    tickets = SupportTicket.objects.all()
    return render(request, 'admin_panel/admin_support_tickets.html', {'tickets': tickets})

# View for managing user feedback
def admin_user_feedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'admin_panel/admin_user_feedback.html', {'feedback': feedback})

# View for managing freelancers
def admin_manage_freelancers(request):
    freelancers = User.objects.filter(user_type='freelancer')
    return render(request, 'admin_panel/admin_manage_freelancers.html', {'freelancers': freelancers})

# View for managing clients
def admin_manage_clients(request):
    clients = User.objects.filter(user_type='client')
    return render(request, 'admin_panel/admin_manage_clients.html', {'clients': clients})

# View for recent activity
def admin_recent_activity(request):
    recent_activity = Activity.objects.all().order_by('-timestamp')[:5]
    return render(request, 'admin_panel/admin_recent_activity.html', {'recent_activity': recent_activity})

# View for checking system health
def admin_system_health(request):
    system_health = SystemHealth.objects.latest('timestamp')
    return render(request, 'admin_panel/admin_system_health.html', {'system_health': system_health})

# View for new registrations
def admin_new_registrations(request):
    new_registrations = User.objects.filter(is_new=True)
    return render(request, 'admin_panel/admin_new_registrations.html', {'new_registrations': new_registrations})
