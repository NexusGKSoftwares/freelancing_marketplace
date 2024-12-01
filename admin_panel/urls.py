from django.urls import path
from . import views

urlpatterns = [
    path('admin_panel/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_panel/manage_users/', views.admin_manage_users, name='admin_manage_users'),
    path('admin_panel/job_postings/', views.admin_job_postings, name='admin_job_postings'),
    path('admin_panel/payments/', views.admin_payments, name='admin_payments'),
    path('admin_panel/system_activity/', views.admin_system_activity, name='admin_system_activity'),
    path('admin_panel/analytics/', views.admin_analytics, name='admin_analytics'),
    path('admin_panel/notifications/', views.admin_notifications, name='admin_notifications'),
    path('admin_panel/support_tickets/', views.admin_support_tickets, name='admin_support_tickets'),
    path('admin_panel/user_feedback/', views.admin_user_feedback, name='admin_user_feedback'),
    path('admin_panel/manage_freelancers/', views.admin_manage_freelancers, name='admin_manage_freelancers'),
    path('admin_panel/manage_clients/', views.admin_manage_clients, name='admin_manage_clients'),
    path('admin_panel/recent_activity/', views.admin_recent_activity, name='admin_recent_activity'),
    path('admin_panel/system_health/', views.admin_system_health, name='admin_system_health'),
    path('admin_panel/new_registrations/', views.admin_new_registrations, name='admin_new_registrations'),
]
