from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request,'accounts/dashboard.html')

def about(request):
    dr = Drone.objects.all()
    return render(request,'accounts/about.html',{'drones':dr})

def customer(request):
    return render(request,'accounts/customer.html')