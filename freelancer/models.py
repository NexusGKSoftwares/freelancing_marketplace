from django.db import models
from django.contrib.auth.models import User

class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2)
    # Using ForeignKey to link each freelancer to a job and feedback (single job per freelancer at a time)
    active_jobs = models.ForeignKey('Job', related_name='active_jobs', null=True, blank=True, on_delete=models.SET_NULL)
    completed_jobs = models.ForeignKey('Job', related_name='completed_jobs', null=True, blank=True, on_delete=models.SET_NULL)
    feedbacks = models.ForeignKey('Feedback', related_name='freelancer_feedbacks', null=True, blank=True, on_delete=models.SET_NULL)
    # Add other fields as needed

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
    # Removed ManyToMany and added ForeignKey to Freelancer for assignment of job to freelancer
    freelancer = models.ForeignKey(Freelancer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Notification(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.freelancer.name}"


class Feedback(models.Model):
    client_name = models.CharField(max_length=255)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.client_name}"
