from django import forms

class ProfilePictureForm(forms.Form):
    picture = forms.ImageField(label="Upload Profile Picture")
