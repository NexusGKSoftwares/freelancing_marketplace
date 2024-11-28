from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'profile_picture', 'bio', 'location', ]  

        
    profile_picture = forms.ImageField(required=False)
