from django.urls import path
from . import views

urlpatterns = [
    path('client_dashboard/', views.client_dashboard, name='client_dashboard'),
    path('jobs_list/', views.jobs, name='jobs'),
    path('post-job/', views.post_job, name='post_job'),
    path('edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('messages/', views.messages_view, name='messages'),
    path('notifications/', views.notifications_view, name='notifications'),
]
