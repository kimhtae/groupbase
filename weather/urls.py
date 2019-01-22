from django.contrib import admin
from django.urls import path, include

from . import views 

urlpatterns = [
    path('weather_search/', views.weather_search, name='weather_search'),
]