from django.db import models
from django.contrib.auth.models import User

# Model for Users (Freelancers and Clients)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    is_freelancer = models.BooleanField(default=False)  # True if freelancer, False if client
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# Model for Job Postings
class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posted_jobs")
    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# Model for Payments
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username}"

# Model for System Activity Logs
class Activity(models.Model):
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    
    def __str__(self):
        return f"{self.action} by {self.user.username} on {self.timestamp}"

# Model for Support Tickets
class SupportTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    subject = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Open', 'Open'), ('Resolved', 'Resolved')])

    def __str__(self):
        return f"Ticket #{self.id}: {self.subject}"

# Model for User Feedback
class UserFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedback")
    rating = models.IntegerField(choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Good'), (4, '4 - Very Good'), (5, '5 - Excellent')])
    comments = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username} on {self.date_submitted}"
