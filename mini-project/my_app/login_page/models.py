from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Register(models.Model):
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    pincode=models.CharField(max_length=6)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"