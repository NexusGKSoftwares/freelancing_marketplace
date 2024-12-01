from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, Message, Notification
from django.contrib.auth.models import User

@login_required
def client_dashboard(request):
    active_jobs = Job.objects.filter(client=request.user, is_active=True).count()
    hired_freelancers = 0  # Placeholder for hired freelancers logic
    unread_messages = Message.objects.filter(recipient=request.user, is_read=False).count()
    recent_activity = Notification.objects.filter(user=request.user).order_by('-timestamp')[:5]
    return render(request, 'client/client_dashboard.html', {
        'active_jobs': active_jobs,
        'hired_freelancers': hired_freelancers,
        'unread_messages': unread_messages,
        'recent_activity': recent_activity,
    })

@login_required
def post_job(request):
    if request.method == 'POST':
        title = request.POST['job_title']
        description = request.POST['job_description']
        budget = request.POST['budget']
        Job.objects.create(client=request.user, title=title, description=description, budget=budget)
        return redirect('client_dashboard')
    return render(request, 'client/post_job.html')

@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, client=request.user)
    if request.method == 'POST':
        job.title = request.POST['job_title']
        job.description = request.POST['job_description']
        job.budget = request.POST['budget']
        job.save()
        return redirect('client_dashboard')
    return render(request, 'client/edit_job.html', {'job': job})

@login_required
def messages_view(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'client/messages.html', {'messages': messages})

@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'client/notifications.html', {'notifications': notifications})
