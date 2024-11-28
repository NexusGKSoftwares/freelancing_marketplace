from django.db import models

# Define the Skill model first
class Skill(models.Model):
    name = models.CharField(max_length=100)  # Name of the skill
    description = models.TextField(blank=True, null=True)  # Optional description of the skill

    def __str__(self):
        return self.name  # Return the name of the skill when displaying it

# Now define the Profile model
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="profiles", blank=True)

    def __str__(self):
        return self.user.username
