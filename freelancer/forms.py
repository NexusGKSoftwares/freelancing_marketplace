from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'location', 'skills', 'profile_picture', 'bio']
        
    profile_picture = forms.ImageField(required=False)
