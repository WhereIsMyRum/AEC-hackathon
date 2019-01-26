from django.contrib import admin
from django.urls import path

from . import views

app_name="home_page"

urlpatterns = [
    path('', views.home, name='home'),
    path('NewObject/', views.newobject, name='newobject'),
    path('search/', views.search, name='search'),
]