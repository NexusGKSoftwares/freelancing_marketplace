# models.py (in your app, e.g., 'freelancer')

from django.db import models
from django.contrib.auth.models import User
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    # skill_ids = models.TextField() 

    def __str__(self):
        return self.user.username


