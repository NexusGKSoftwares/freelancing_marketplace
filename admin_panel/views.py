from django.shortcuts import get_object_or_404, render, redirect
from django.db import connection
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import AddUserForm  
from .models import Project  
from .forms import ProjectForm  
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserSettings

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Query the database for the admin user
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, password FROM admins WHERE username = %s", [username])
            admin = cursor.fetchone()

        # Validate the user and password
        if admin and check_password(password, admin[1]):
            # Store admin session
            request.session['admin_id'] = admin[0]
            return redirect("/admin_panel/dashboard/")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "admin_panel/login.html")


def dashboard(request):
    # Ensure admin is logged in
    if 'admin_id' not in request.session:
        return redirect('/admin_panel/login/')
    return render(request, 'admin_panel/dashboard.html')


# User Management View
def user_management(request):
    """
    View for displaying and managing users.
    Includes options for viewing, editing, and suspending users.
    """
    # Fetch all users
    users = User.objects.all()

    context = {
        "users": users,
    }
    return render(request, "admin_panel/user_management.html", context)

def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User added successfully!")
            return redirect('user_management')  # Redirect to the user management page
    else:
        form = AddUserForm()
    return render(request, 'admin_panel/add_user.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Ensure that only superusers or admins can delete users
    if request.user.is_superuser:
        user.delete()
        messages.success(request, "User deleted successfully.")
    else:
        messages.error(request, "You do not have permission to delete users.")
    
    return redirect('user_management')

# View User Profile
def view_user(request, user_id):
    """
    View for displaying the details of a single user.
    """
    user = get_object_or_404(User, id=user_id)
    return render(request, "admin_panel/view_user.html", {"user": user})

# Edit User Profile
def edit_user(request, user_id):
    """
    View for editing a user's profile information.
    """
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.first_name = request.POST.get("first_name", user.first_name)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.email = request.POST.get("email", user.email)
        user.save()
        messages.success(request, "User profile updated successfully!")
        return redirect("user_management")

    return render(request, "admin_panel/edit_user.html", {"user": user})

# Suspend or Activate User
def toggle_user_status(request, user_id):
    """
    Toggle the active status of a user (activate/suspend).
    """
    user = get_object_or_404(User, id=user_id)
    user.is_active = not user.is_active
    user.save()
    status = "activated" if user.is_active else "suspended"
    messages.success(request, f"User has been {status}.")
    return redirect("user_management")



# View all projects
def project_management(request):
    projects = Project.objects.all()  # Adjust query as needed
    return render(request, 'admin_panel/project_management.html', {'projects': projects})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            print("Form is valid, saving project")
            form.save()
            return redirect('project_management')
        else:
            print("Form errors: ", form.errors)  # Print out form errors
    else:
        form = ProjectForm()
    return render(request, 'admin_panel/add_project.html', {'form': form})

# View individual project details
def view_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'admin_panel/view_project.html', {'project': project})

# Edit project details
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        project.name = request.POST['name']
        project.description = request.POST['description']
        project.status = request.POST['status']  # Assuming status field exists
        project.save()
        messages.success(request, "Project updated successfully.")
        return redirect('project_management')
    
    return render(request, 'admin_panel/edit_project.html', {'project': project})

# Delete a project
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.user.is_superuser:
        project.delete()
        messages.success(request, "Project deleted successfully.")
    else:
        messages.error(request, "You do not have permission to delete this project.")
    
    return redirect('project_management')



def system_settings(request):
    user_settings = UserSettings.objects.get(user=request.user)
    
    if request.method == 'POST':
        # Update user settings from the form
        user_settings.language = request.POST.get('language')
        user_settings.timezone = request.POST.get('timezone')
        user_settings.notifications_enabled = 'notifications_enabled' in request.POST
        user_settings.dark_mode = 'dark_mode' in request.POST
        if 'profile_picture' in request.FILES:
            user_settings.profile_picture = request.FILES['profile_picture']
        user_settings.save()
        return redirect('system_settings')
    
    return render(request, 'system_settings.html', {'settings': user_settings})
