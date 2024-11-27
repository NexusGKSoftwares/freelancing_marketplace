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
from django.urls import path

from freelancer import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.freelancer_register, name='freelancer_register'),
    path('check_username/', views.check_username, name='check_username'),
    path('login/', views.freelancer_login, name='freelancer_login'),
    path('dashboard/', views.dashboard, name='freelancer_dashboard'),
    path('logout/', views.freelancer_logout, name='freelancer_logout'),
]
