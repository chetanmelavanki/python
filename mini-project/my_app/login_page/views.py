from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .form import LoginForm
from .form import RegistrationForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def login_view(request):
    form = LoginForm(request)
    return render(request, 'login.html', {'form': form})

def website(request):
    return render(request,'webpage.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    register_form = RegistrationForm()  # Create an empty form instance
    return render(request, 'register.html', {'register_form': register_form})
