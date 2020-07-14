from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import MissionFilter
from django.contrib.auth.forms import UserCreationForm

def home(request):
    customer = Customer.objects.all()
    mission = Mission.objects.all()
    context = {
        'customer': customer,
        # 'mymission':mymission,
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
    somedict = {'customer': customer, 'missions': mission,
                'total_mission': total_mission}
    return render(request, 'accounts/customer.html', somedict)


def mission(request):

    mission = Mission.objects.all()
    myFilter = MissionFilter(request.GET, queryset=mission)
    mission = myFilter.qs
    context = {
        'myFilter': myFilter,
        'missions': mission,
    }
    return render(request, 'accounts/allorder.html', context)


def launch(request, pk):
    mission = Mission.objects.get(id=pk)
    context = {
        'mission': mission
    }
    return render(request, 'accounts/launch.html', context)
    # This is for the launch function


def createMission(request):

    form = MissionForm()
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'accounts/mission_form.html', context)


def updateMission(request, pk):

    mission = Mission.objects.get(id=pk)
    form = MissionForm(instance=mission)
    if request.method == 'POST':
        form = MissionForm(request.POST, instance=mission)
        if form.is_valid():
            form.save()
            return redirect('all-mission')
    context = {
        'form': form,

    }
    return render(request, 'accounts/mission_form.html', context)


def status(request):
    customer = Customer.objects.all()
    mission = Mission.objects.all()
    context = {
        'customer': customer,
        # 'mymission':mymission,
        'mission': mission,
        'total_drone': Drone.objects.all().count(),
        'maintenance_drone': Drone.objects.filter(status="m").count(),
        'mission_complete': Mission.objects.filter(mission_status="Complete").count(),
        'mission_pending': Mission.objects.filter(mission_status="Pending").count(),
        'mission_cancelled': Mission.objects.filter(mission_status="Cancelled").count(),
    }
    return render(request, 'accounts/status.html', context)


def createCustomer(request):

    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form, }
    return render(request, 'accounts/mission_form.html', context)


def updateCustomer(request, pk):

    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/mission_form.html', context)


def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)
