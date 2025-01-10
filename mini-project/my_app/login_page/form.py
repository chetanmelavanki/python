# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    
class RegistrationForm(forms.Form):
    first_name=forms.CharField(max_length=50)
    middle_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email=forms.CharField(max_length=50)
    mobile_number=forms.CharField(max_length=10)
    address=forms.CharField(max_length=100)
    pincode=forms.CharField(max_length=6)
    