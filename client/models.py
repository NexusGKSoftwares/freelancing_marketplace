from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('proposal', 'Proposal'),
        ('design', 'Design'),
        ('development', 'Development'),
        ('testing', 'Testing'),
        ('deployed', 'Deployed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='proposal')
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Notification(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.username}: {self.message}"

class Invoice(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice for {self.project.title}"

class Feedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='feedback')
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # e.g., 1-5 stars
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)