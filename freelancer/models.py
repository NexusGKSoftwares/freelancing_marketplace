# models.py
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    freelancer = models.ForeignKey('Freelancer', related_name='feedbacks', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.freelancer.name}"


class Freelancer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Linking to the built-in User model for authentication
    name = models.CharField(max_length=100)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active_jobs = models.ForeignKey(Job, related_name='active_freelancers', null=True, blank=True, on_delete=models.SET_NULL)
    completed_jobs = models.ForeignKey(Job, related_name='completed_freelancers', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

