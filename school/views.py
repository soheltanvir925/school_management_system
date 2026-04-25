from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
#from .models import Notification

# Create your views here.

def index(request):
    return render(request, "authentication/login.html")

def dashboard(request):
    return render(request, "students/student-dashboard.html")


#def index(request):
#    return render(request, 'Home/index.html')
