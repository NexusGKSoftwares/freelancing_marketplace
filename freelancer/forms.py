from django import forms
from .models import ModelName

class ModelForm(forms.ModelForm):
    class Meta:
        model = ModelName
        fields = ('__all__')