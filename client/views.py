from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import ClientProfile, Project, Notification, Invoice
from django.contrib import messages

@login_required
def client_dashboard(request):
    projects = Project.objects.filter(client=request.user)
    notifications = Notification.objects.filter(client=request.user, is_read=False)
    return render(request, 'clients/dashboard.html', {
        'projects': projects,
        'notifications': notifications
    })

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id, client=request.user)
    return render(request, 'clients/project_detail.html', {'project': project})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(client=request.user)
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return render(request, 'clients/notifications.html', {'notifications': notifications})

@login_required
def invoices(request):
    invoices = Invoice.objects.filter(project__client=request.user)
    return render(request, 'clients/invoices.html', {'invoices': invoices})

@login_required
def project_feedback(request, project_id):
    project = get_object_or_404(Project, id=project_id, client=request.user)
    if request.method == "POST":
        feedback = request.POST['feedback']
        # Save feedback to database or process as needed
        messages.success(request, "Thank you for your feedback!")
        return redirect('dashboard')
    return render(request, 'clients/project_feedback.html', {'project': project})
