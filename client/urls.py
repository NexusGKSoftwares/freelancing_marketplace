from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.client_register, name='register'),
    path('login/', views.client_login, name='login'),
    # path('logout/', views.client_logout, name='logout'),
    path('client_dashboard/', views.client_dashboard, name='client_dashboard'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('notifications/', views.notifications, name='notifications'),
    path('invoices/', views.invoices, name='invoices'),
    path('project/<int:project_id>/feedback/', views.project_feedback, name='project_feedback'),
    path('profile/', views.client_profile, name='client_profile'),
]
