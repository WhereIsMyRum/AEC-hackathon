from django.contrib import admin
from django.urls import path

from . import views

app_name="home_page"

urlpatterns = [
    path('', views.change, name='change'),
]