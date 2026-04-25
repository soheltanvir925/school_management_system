from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from customers import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_school, name='register'),
]
