from django.db import models
from django.contrib.auth.models import User



class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='freelancer_profile')
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Job(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Available', 'Available'),
        ('Pending', 'Pending'),
    ]

    freelancer = models.ForeignKey(Freelancer, on_delete=models.SET_NULL, null=True, blank=True, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def status_class(self):
        """Returns a CSS class based on the job status."""
        status_classes = {
            'Active': 'badge-warning',
            'Completed': 'badge-success',
            'Available': 'badge-primary',
            'Pending': 'badge-secondary',
        }
        return status_classes.get(self.status, 'badge-light')

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"

class Feedback(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, related_name='feedbacks')
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='given_feedbacks')
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.freelancer.user.username} by {self.client.username if self.client else 'Unknown'}"
class Payment(models.Model):
    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]

    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='Pending')
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.freelancer.name} - {self.amount} ({self.status})"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
