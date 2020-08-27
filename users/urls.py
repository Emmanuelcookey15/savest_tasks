"""Defines URL patterns for users"""
from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    path('send_email/', views.send_email, name='send_email'),
    path('', views.index, name='index'),
]
