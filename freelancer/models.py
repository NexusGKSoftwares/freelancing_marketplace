# models.py (in your app, e.g., 'freelancer')

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name