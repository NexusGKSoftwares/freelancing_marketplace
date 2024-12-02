from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', views.freelancer_dashboard, name='freelancer_dashboard'),
    path('profile/edit/', views.freelancer_edit_profile, name='freelancer_edit_profile'),
    path('payments/', views.freelancer_payment_overview, name='freelancer_payment_overview'),
    path('active-jobs/', views.freelancer_ongoing_jobs, name='freelancer_ongoing_jobs'),
    path('available-jobs/', views.freelancer_available_jobs, name='freelancer_available_jobs'),
    path('notifications/', views.freelancer_notifications, name='freelancer_notifications'),
    path('feedback/', views.freelancer_feedback, name='freelancer_feedback'),
    path('job/<int:job_id>/', views.freelancer_job_details, name='freelancer_job_details'),
    path('payment-history/', views.freelancer_payment_history, name='freelancer_payment_history'),
    path('job-history/', views.freelancer_job_history, name='freelancer_job_history'),
]
