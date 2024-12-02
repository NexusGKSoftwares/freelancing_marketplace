from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Freelancer, Job, Notification, Feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'freelancer/index.html')
    else:
        return HttpResponseRedirect(reverse('freelancer_dashboard'))
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = request.POST.get('role')  # Set role based on form input
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
@login_required
def freelancer_dashboard(request):
    # Assuming the user is logged in
    freelancer = Freelancer.objects.get(user=request.user)  # Use related 'user' field here
    available_jobs_count = Job.objects.filter(is_available=True).count()
    notifications = Notification.objects.filter(freelancer=freelancer)
    
    # Calculate earnings and pass the data for the chart
    earnings_data = [100, 200, 300, 400]  # Example earnings data
    earnings_labels = ['January', 'February', 'March', 'April']  # Example labels for earnings

    return render(request, 'freelancer/dashboard.html', {
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
