from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage_users/', views.admin_manage_users, name='admin_manage_users'),
    path('job_postings/', views.admin_job_postings, name='admin_job_postings'),
    path('payments/', views.admin_payments, name='admin_payments'),
    path('system_activity/', views.admin_system_activity, name='admin_system_activity'),
    path('analytics/', views.admin_analytics, name='admin_analytics'),
    path('notifications/', views.admin_notifications, name='admin_notifications'),
    path('support_tickets/', views.admin_support_tickets, name='admin_support_tickets'),
    path('user_feedback/', views.admin_user_feedback, name='admin_user_feedback'),
    path('manage_freelancers/', views.admin_manage_freelancers, name='admin_manage_freelancers'),
    path('manage_clients/', views.admin_manage_clients, name='admin_manage_clients'),
    path('recent_activity/', views.admin_recent_activity, name='admin_recent_activity'),
    path('system_health/', views.admin_system_health, name='admin_system_health'),
    path('new_registrations/', views.admin_new_registrations, name='admin_new_registrations'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
