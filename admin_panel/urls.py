from django.urls import path
from . import views

urlpatterns = [
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/manage_users/', views.admin_manage_users, name='admin_manage_users'),
    path('admin/job_postings/', views.admin_job_postings, name='admin_job_postings'),
    path('admin/payments/', views.admin_payments, name='admin_payments'),
    path('admin/system_activity/', views.admin_system_activity, name='admin_system_activity'),
    path('admin/analytics/', views.admin_analytics, name='admin_analytics'),
    path('admin/notifications/', views.admin_notifications, name='admin_notifications'),
    path('admin/support_tickets/', views.admin_support_tickets, name='admin_support_tickets'),
    path('admin/user_feedback/', views.admin_user_feedback, name='admin_user_feedback'),
    path('admin/manage_freelancers/', views.admin_manage_freelancers, name='admin_manage_freelancers'),
    path('admin/manage_clients/', views.admin_manage_clients, name='admin_manage_clients'),
    path('admin/recent_activity/', views.admin_recent_activity, name='admin_recent_activity'),
    path('admin/system_health/', views.admin_system_health, name='admin_system_health'),
    path('admin/new_registrations/', views.admin_new_registrations, name='admin_new_registrations'),
]
