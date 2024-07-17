from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path("home",views.index,name='home'),
    path("",views.empty,name='home'),
    path("services",views.services,name='services'),
]