from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import FoodListing, Request, Food, Donor, Receiver
from .forms import FoodListingForm, RequestForm
from django.contrib.auth.forms import UserCreationForm

# Dashboard view
@login_required
def dashboard(request):
    food_listings = FoodListing.objects.all()
    return render(request, 'dashboard.html', {'food_listings': food_listings})

# Add food view
@login_required
def add_food(request):
    if request.method == 'POST':
        food_name = request.POST.get('name')
        description = request.POST.get('description')
        location = request.POST.get('location')

        if food_name:
            food = Food(name=food_name, description=description, location=location)
            food.donor = request.user.donor
            food.save()
            return redirect('food_list')

    return render(request, 'add_food.html')

# Request food view
@login_required
def request_food(request, pk):
    food_listing = get_object_or_404(FoodListing, pk=pk)
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.food_listing = food_listing
            request_obj.receiver = request.user.receiver
            request_obj.save()
            return redirect('dashboard')
    else:
        form = RequestForm()
    return render(request, 'request_food.html', {'form': form, 'food_listing': food_listing})

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Donor.objects.create(user=user)  # Create donor profile
            login(request, user)  # Log the user in
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

# User login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect after successful login
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')  # Show error message if login fails

    return render(request, 'login.html')

# Food list view
@login_required
def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})
