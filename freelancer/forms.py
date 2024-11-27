from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'location', 'skills', 'profile_picture', 'bio']
        
    profile_picture = forms.ImageField(required=False)
