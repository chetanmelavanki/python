from django import forms
from .models import FoodListing, Request

# Food listing form
class FoodListingForm(forms.ModelForm):
    class Meta:
        model = FoodListing
        fields = ['food_name', 'quantity', 'description', 'location', 'expiration_date']

# Request form
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['food_listing']
