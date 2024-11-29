from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import ClientProfile, Project, Notification, Invoice
from django.contrib import messages
from .forms import FeedbackForm

def client_register(request):
    return render(request, 'client/register.html')

def client_login(request):
    return render(request, 'client/login.html')

@login_required
def client_dashboard(request):
    projects = Project.objects.filter(client=request.user)
    notifications = Notification.objects.filter(client=request.user, is_read=False)
    return render(request, 'client/client_dashboard.html', {
        'projects': projects,
        'notifications': notifications
    })

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id, client=request.user)
    return render(request, 'client/project_detail.html', {'project': project})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(client=request.user)
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return render(request, 'client/notifications.html', {'notifications': notifications})

@login_required
def invoices(request):
    invoices = Invoice.objects.filter(project__client=request.user)
    return render(request, 'client/invoices.html', {'invoices': invoices})



def project_feedback(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.project = project
            feedback.client = request.user  # Assuming logged-in client
            feedback.save()
            return redirect('dashboard')
    else:
        form = FeedbackForm()

    return render(request, 'client/project_feedback.html', {'form': form, 'project': project})
def client_profile(request):
    # Your logic for the client profile page
    return render(request, 'client/client_profile.html')