from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    language = models.CharField(max_length=50, default='en')
    timezone = models.CharField(max_length=50, default='UTC')
    notifications_enabled = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s settings"
