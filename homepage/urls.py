from django.contrib import admin
from django.urls import path

from . import views

app_name="home_page"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
]