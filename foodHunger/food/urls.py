from django.urls import path
from . import views
urlpatterns = [
    path('', views.food,name='food'),
    path('home/',views.foodHome, name = 'home'),
    # path('register',views.register, name = 'register'),
    path('hotelRegistration', views.registerHotel,name='hotelRegistration'),
    path('login/',views.userLogin,name='login'),
    path('dashboard/',views.dashboardDetails,name='dashboard'),
    # path('dashboard/dashboardPost',views.dashboardPost,name='dashboardPost'),
    path('logout/',views.logout,name='logout'),
    path('userRegistration/',views.userRegistration,name='userRegistration'),
    path('distributeFood/',views.distributeFood,name='distributeFood'),
    path('hotels/',views.hotels,name='hotels'),
    path('hotelSummary/<str:registrationNumber>',views.hotelSummary,name="hotelSummary")
]