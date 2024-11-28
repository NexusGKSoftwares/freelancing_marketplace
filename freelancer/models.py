# models.py (in your app, e.g., 'freelancer')

from django.db import models
from django.contrib.auth.models import User
class Skill(models.Model):
    name = models.CharField(max_length=100)  # Name of the skill
    description = models.TextField(blank=True, null=True)  # Optional description of the skill

    def __str__(self):
        return self.name 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="profiles", blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'
    
class SkillProfile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
