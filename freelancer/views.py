from django.shortcuts import render
from .models import Freelancer, Job, Notification, Feedback
from django.contrib.auth.decorators import login_required

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'freelancer/index.html')
    else:
        return HttpResponseRedirect(reverse('freelancer_dashboard'))
    
@login_required
def freelancer_dashboard(request):
    freelancer = Freelancer.objects.get(user=request.user)
    notifications = Notification.objects.filter(freelancer=freelancer)
    available_jobs_count = Job.objects.filter(status='available').count()
    earnings_labels = ["January", "February", "March", "April", "May"]
    earnings_data = [1000, 1500, 2000, 1800, 2500]  # Example data
    context = {
        'freelancer': freelancer,
        'notifications': notifications,
        'available_jobs_count': available_jobs_count,
        'earnings_labels': earnings_labels,
        'earnings_data': earnings_data,
    }
    return render(request, 'freelancer_dashboard.html', context)

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
