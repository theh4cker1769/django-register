from django.contrib import admin
from django.urls import path, include
from rome import views

urlpatterns = [
    path('', views.user_register, name='user_register')
]