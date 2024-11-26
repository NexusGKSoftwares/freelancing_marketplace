from django.db import models

# Status choices for a project
class ProjectStatus(models.TextChoices):
    ONGOING = 'ongoing', 'Ongoing'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'

class Project(models.Model):
    # Project name
    name = models.CharField(max_length=200)
    
    # Project description
    description = models.TextField()
    
    # Project status (using choices for predefined statuses)
    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.ONGOING
    )
    
    # Start date of the project
    start_date = models.DateField()
    
    # End date of the project (can be nullable)
    end_date = models.DateField(null=True, blank=True)
    
    # Date the project was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Date the project was last updated
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at']

    # Optional: method to get the project status display
    def get_status_display(self):
        return dict(ProjectStatus.choices).get(self.status, 'Unknown')
