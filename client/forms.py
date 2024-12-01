from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'category', 'type', 'min_budget', 'max_budget', 'skills', 'status']
        widgets = {
            'skills': forms.Textarea(attrs={'placeholder': 'Enter skills as a comma-separated list (e.g., Python, Django, HTML)'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
