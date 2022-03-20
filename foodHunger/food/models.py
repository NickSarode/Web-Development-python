from pyexpat import model
from django.db import models

# Create your models here.
class HotelDetails(models.Model):
    hotel = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'pics')
    password = models.CharField(max_length=100)
    confirmPassword = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    zipCode = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    countryCode = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=100)
    registrationNumber = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=200)
    star = models.CharField(max_length=500)

class foodDetails(models.Model):
    registrationNumber = models.CharField(max_length=100)
    hotel = models.CharField(max_length=200)
    foodBoxes = models.PositiveIntegerField(default=0)
    food = models.CharField(max_length=5000)
    date = models.DateField()
    availableStatus = models.PositiveIntegerField(default=0)

class userFoodRegistration(models.Model):
    registrationNumber = models.CharField(max_length=100)
    hotel = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    date = models.DateField()
    alphaString = models.CharField(max_length=20)
    status = models.PositiveIntegerField(default=0)
