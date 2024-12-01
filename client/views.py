from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, Message, Notification
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import JobForm

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
    job = Job()  # Create an instance to access the model choices
    if request.method == 'POST':
        # Handle job form submission
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        job_type = request.POST.get('type')
        min_budget = request.POST.get('min_budget')
        max_budget = request.POST.get('max_budget')
        skills = request.POST.get('skills').split(',')  # Convert comma-separated skills into a list

        # Create a Job object for preview
        job_preview = {
            'title': title,
            'description': description,
            'category': category,
            'job_type': job_type,
            'min_budget': min_budget,
            'max_budget': max_budget,
            'skills': skills
        }

        # Save the job preview in the session (to persist data between requests)
        request.session['job_preview'] = job_preview

        # Redirect to the preview page
        return redirect('preview_and_post_job')

    return render(request, 'client/post_job.html', {
        'job': job,  # Pass the Job instance to the template
    })
def preview_and_post_job(request):
    # Retrieve the job preview from session
    job_preview = request.session.get('job_preview')

    if not job_preview:
        return redirect('post_job')  # If no preview data exists, redirect back to the post job page

    if request.method == 'POST':
        # Save the job to the database
        job = Job(
            title=job_preview['title'],
            description=job_preview['description'],
            category=job_preview['category'],
            type=job_preview['job_type'],
            min_budget=job_preview['min_budget'],
            max_budget=job_preview['max_budget'],
            skills=job_preview['skills'],
            client=request.user  # Assuming the user is logged in
        )
        job.save()

        # Clear the session data
        del request.session['job_preview']

        # Redirect to the jobs listing page or success page
        return redirect('job_list')  # Assuming you have a 'jobs_page' URL

    return render(request, 'client/preview_job.html', {'job_preview': job_preview})

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




def job_list(request):
    # Get filters from request
    search = request.GET.get('search', '')
    category = request.GET.get('category', '')
    budget = request.GET.get('budget', '')
    job_type = request.GET.get('job_type', '')

    # Filter jobs based on user input
    jobs = Job.objects.all()
    if search:
        jobs = jobs.filter(title__icontains=search)
    if category:
        jobs = jobs.filter(category=category)
    if budget:
        min_budget, max_budget = map(int, budget.split('-'))
        jobs = jobs.filter(min_budget__gte=min_budget, max_budget__lte=max_budget)
    if job_type:
        jobs = jobs.filter(type=job_type)

    # Paginate the job list
    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {'jobs': page_obj}
    return render(request, 'client/jobs.html', context)

def filter_jobs(request):
    if request.method == 'POST':
        search = request.POST.get('search', '')
        category = request.POST.get('category', '')
        budget = request.POST.get('budget', '')
        job_type = request.POST.get('job_type', '')

        jobs = Job.objects.all()
        if search:
            jobs = jobs.filter(title__icontains=search)
        if category:
            jobs = jobs.filter(category=category)
        if budget:
            min_budget, max_budget = map(int, budget.split('-'))
            jobs = jobs.filter(min_budget__gte=min_budget, max_budget__lte=max_budget)
        if job_type:
            jobs = jobs.filter(type=job_type)

        context = {'jobs': jobs}
        return render(request, 'client/jobs.html', context)
    
def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'client/job_detail.html', {'job': job})

# Edit Job View
def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_detail', job_id=job.id)
    else:
        form = JobForm(instance=job)
    return render(request, 'client/edit_job.html', {'form': form, 'job': job})

# Delete Job View
def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')  # Redirect to job list after deletion
    return redirect('job_detail', job_id=job.id)