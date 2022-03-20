from django.contrib import admin
from .models import HotelDetails,foodDetails,userFoodRegistration
# Register your models here.

admin.site.register(HotelDetails)
admin.site.register(foodDetails)
admin.site.register(userFoodRegistration)