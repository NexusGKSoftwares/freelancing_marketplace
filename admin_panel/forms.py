# from django import forms
# from django.contrib.auth.models import User
# # from .models import Project, StaticPage

# class AddUserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'password']
# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['name', 'description', 'status', 'start_date', 'end_date']


# class StaticPageForm(forms.ModelForm):
#     class Meta:
#         model = StaticPage
#         fields = ['title', 'content']

#     # Customizing form fields if needed
#     title = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}), required=True)
