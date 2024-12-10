from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.freelancer_login, name='login'),
    path('dashboard/', views.freelancer_dashboard, name='freelancer_dashboard'),
    path('profile/', views.freelancer_profile, name='freelancer_profile'),
    path('upload-profile-picture/', views.upload_profile_picture, name='upload_profile_picture'),
    path('toggle_user_status/<int:user_id>/', views.toggle_freelancer_status, name='toggle_freelancer_status'),
    path('edit_user/<int:user_id>/', views.freelancer_edit_user, name='freelancer_edit_user'),
    path('payments/', views.freelancer_payment_overview, name='freelancer_payment_overview'),
    path('active-jobs/', views.freelancer_ongoing_jobs, name='freelancer_ongoing_jobs'),
    path('available-jobs/', views.freelancer_available_jobs, name='freelancer_available_jobs'),
    path('notifications/', views.freelancer_notifications, name='freelancer_notifications'),
    path('feedback/', views.freelancer_feedback, name='freelancer_feedback'),
    path('job/<int:job_id>/', views.freelancer_job_details, name='freelancer_job_details'),
    path('apply-for-job/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('payment-history/', views.freelancer_payment_history, name='freelancer_payment_history'),
    path('job-history/', views.freelancer_job_history, name='freelancer_job_history'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('features/', views.features, name='features'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('faq/', views.faq, name='faq'),
]+ static (settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)