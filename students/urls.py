from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student_list/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('students/<str:slug>/', views.student_details, name='student_details'),
    path('edit/<str:slug>/', views.edit_student, name='edit_student'),
    path('delete/<str:slug>/', views.delete_student, name='delete_student'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    
]
