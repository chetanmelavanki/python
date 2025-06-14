from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='donor')
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Receiver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_organization = models.BooleanField(default=False)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

class FoodListing(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    location = models.CharField(max_length=200)
    expiration_date = models.DateTimeField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_name} by {self.donor.user.username}"

class Request(models.Model):
    food_listing = models.ForeignKey(FoodListing, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"{self.receiver.user.username} requested {self.food_listing.food_name}"

class Food(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    location = models.CharField(max_length=255)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return self.name
