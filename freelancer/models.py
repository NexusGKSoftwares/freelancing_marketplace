from django.db import models
from django.contrib.auth.models import User

class Freelancer(models.Model):
    name = models.CharField(max_length=255)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2)
    active_jobs = models.ManyToManyField(
        'Job',
        related_name='active_jobs',  # Add a custom related_name
        blank=True,
    )
    completed_jobs = models.ManyToManyField(
        'Job',
        related_name='completed_jobs',  # Add a custom related_name
        blank=True,
    )
    feedbacks = models.ManyToManyField('Feedback')

    def __str__(self):
        return self.name
class Job(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    deadline = models.DateTimeField()
    freelancer = models.ForeignKey(Freelancer, on_delete=models.SET_NULL, null=True, blank=True)

class Notification(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    client_name = models.CharField(max_length=255)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
