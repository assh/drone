from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    customer = Customer.objects.all()
    mission = Mission.objects.all()
    context = {
        'customer': customer,
        #'mymission':mymission,
        'mission': mission,
        'total_drone': Drone.objects.all().count(),
        'maintenance_drone': Drone.objects.filter(status="m").count(),
        'mission_complete': Mission.objects.filter(mission_status="Complete").count(),
        'mission_pending': Mission.objects.filter(mission_status="Pending").count(),
        'mission_cancelled': Mission.objects.filter(mission_status="Cancelled").count(),
    }
    return render(request, 'accounts/dashboard.html', context)


def about(request):
    dr = Drone.objects.all()
    return render(request, 'accounts/about.html', {'drones': dr})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    mission = customer.mission_set.all()
    total_mission = mission.count()
    somedict = {'customer': customer, 'missions': mission,'total_mission':total_mission}
    return render(request, 'accounts/customer.html', somedict)

def mission(request):
    mission = Mission.objects.all()
    context = {
        'missions':mission,
    }
    return render(request,'accounts/allorder.html',context)