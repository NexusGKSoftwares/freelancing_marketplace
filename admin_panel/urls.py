"""
URL configuration for freelancing_marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from admin_panel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("user_management/", views.user_management, name="user_management"),
    path('add_user/', views.add_user, name='add_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path("user/<int:user_id>/view/", views.view_user, name="view_user"),
    path("user/<int:user_id>/edit/", views.edit_user, name="edit_user"),
    path("user/<int:user_id>/toggle_status/", views.toggle_user_status, name="toggle_user_status"),
    path('project_management/', views.project_management, name='project_management'),
    path('project_management/add/', views.add_project, name='add_project'), 
    path('view_project/<int:project_id>/', views.view_project, name='view_project'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('system_settings/', views.system_settings, name='system_settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)