from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    institution = forms.CharField(max_length=255)
    designation = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    state = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'institution', 
                  'designation', 'phone', 'state', 
                  'password1', 'password2']