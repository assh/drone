from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    context = {
        'customer': Customer.objects.all(), 
        'mission': Mission.objects.all(),
        'total_drone':Drone.objects.all().count(),
        'maintenance_drone':Drone.objects.filter(status="m").count(),
        'mission_complete': Mission.objects.filter(mission_status="Complete").count(),
        'mission_pending': Mission.objects.filter(mission_status="Pending").count(),
        'mission_cancelled': Mission.objects.filter(mission_status="Cancelled").count(),
    }
    return render(request, 'accounts/dashboard.html',context)


def about(request):
    dr = Drone.objects.all()
    return render(request, 'accounts/about.html', {'drones': dr})


def customer(request):
    somedict = {
        'cust': Customer.objects.all(),
        'mission': Mission.objects.all()
    }
    return render(request, 'accounts/customer.html', somedict)
