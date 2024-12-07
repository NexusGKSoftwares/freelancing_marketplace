from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_user/', views.add_user, name='add_user'),
    path('view_user/<int:user_id>/', views.view_user, name='view_user'),  
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'), 
    path('toggle_user_status/<int:user_id>/', views.toggle_user_status, name='toggle_user_status'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('manage_users/', views.admin_manage_users, name='admin_manage_users'),
    path('job_postings/', views.job_postings_overview, name='job_postings'),
    path('admin_payments/', views.payment_management, name='admin_payments'),
    path('admin_system_activity/', views.system_activity, name='admin_system_activity'),
    path('admin_analytics/', views.analytics, name='admin_analytics'),
    path('admin_notifications/', views.notifications, name='admin_notifications'),
    path('admin_support_tickets/', views.support_tickets, name='admin_support_tickets'),
    path('admin_user_feedback/', views.user_feedback, name='admin_user_feedback'),
    path('admin_manage_freelancers/', views.manage_freelancers, name='admin_manage_freelancers'),
    path('admin_manage_clients/', views.manage_clients, name='admin_manage_clients'),
    path('admin_system_health/', views.system_health, name='admin_system_health'),
    path('admin_new_registrations/', views.new_registrations, name='admin_new_registrations'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
