from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import MissionFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from .decorators import unauthenticated_user


@login_required(login_url='login')
#@allowed_user(allowed=['admin'])
def home(request):
    customer = Customer.objects.all()
    mission = Mission.objects.all().order_by('-mission_id')
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


@login_required(login_url='login')
def about(request):
    dr = Drone.objects.all()
    return render(request, 'accounts/about.html', {'drones': dr})

@login_required(login_url='login')
def customer_list(request):
    customer = Customer.objects.all()
    context ={
        'customers':customer
    }
    return render(request,'accounts/customer_list.html',context)

@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    mission = customer.mission_set.all()
    total_mission = mission.count()
    somedict = {'customer': customer, 'missions': mission,
                'total_mission': total_mission}
    return render(request, 'accounts/customer.html', somedict)


def is_valid(user):
    return user.groups.filter(name='Admin').exists()

@login_required(login_url='login')
def mission(request):
    
    mission = Mission.objects.all()
    myFilter = MissionFilter(request.GET, queryset=mission)
    mission = myFilter.qs
    context = {
        'myFilter': myFilter,
        'missions': mission,
    }
    return render(request, 'accounts/allorder.html', context)


@login_required(login_url='login')
def launch(request, pk):
    mission = Mission.objects.get(id=pk)
    context = {
        'mission': mission
    }
    return render(request, 'accounts/launch.html', context)
    # This is for the launch function


@login_required(login_url='login')
def createMission(request):

    form = Mission2Form()
    if request.method == 'POST':
        form = Mission2Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'accounts/mission_form.html', context)


@login_required(login_url='login')
def updateMission(request, pk):

    mission = Mission.objects.get(id=pk)
    form = MissionForm(instance=mission)
    if request.method == 'POST':
        form = MissionForm(request.POST, request.FILES, instance=mission)
        if form.is_valid():
            form.save()
            return redirect('all-mission')
    context = {
        'form': form,

    }
    return render(request, 'accounts/mission_update_form.html', context)


@login_required(login_url='login')
def status(request):
    customer = Customer.objects.all()
    mission = Mission.objects.all()
    context = {
        'customer': customer,
        # 'mymission':mymission,
        'mission': mission,
        'total_missions':Mission.objects.all().count(),
        'total_drone': Drone.objects.all().count(),
        'maintenance_drone': Drone.objects.filter(status="m").count(),
        'onloan_drone': Drone.objects.filter(status="o").count(),
        'available_drone': Drone.objects.filter(status="a").count(),
        'reserved_drone': Drone.objects.filter(status="r").count(),
        'mission_complete': Mission.objects.filter(mission_status="Complete").count(),
        'mission_pending': Mission.objects.filter(mission_status="Pending").count(),
        'mission_cancelled': Mission.objects.filter(mission_status="Cancelled").count(),
    }
    return render(request, 'accounts/status.html', context)


@login_required(login_url='login')
def createCustomer(request):

    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form, }
    return render(request, 'accounts/customer_form.html', context)


@login_required(login_url='login')
def updateCustomer(request, pk):

    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/customer_form.html', context)


@unauthenticated_user
def registerPage(request):

    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created')
            return redirect('register-redirect')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main-home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def createDrone(request):

    form = DroneForm()
    if request.method == 'POST':
        form = DroneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'accounts/drone_form.html', context)

@login_required(login_url='login')
def updateDrone(request, pk):

    drone = Drone.objects.get(id=pk)
    form = DroneForm(instance=drone)
    if request.method == 'POST':
        form = DroneForm(request.POST, instance=drone)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/drone_form.html', context)


@login_required(login_url='login')
def mymission(request):

    mission = Mission.objects.all().filter(manager=request.user)
    myFilter = MissionFilter(request.GET, queryset=mission)
    mission = myFilter.qs
    context = {
        'myFilter': myFilter,
        'missions': mission,
    }
    return render(request, 'accounts/mymission.html', context)

@login_required(login_url='login')
def my_drone(request,pk):

    drone = Drone.objects.get(id=pk)
    form = MyDroneForm(instance=drone)
    context = {
        'drone':drone,
        'form':form,
    }
    return render(request,'accounts/my_drone.html',context)

@login_required(login_url='login')
def launch_drone(request,pk):
    mission = Mission.objects.get(id=pk)
    form = LaunchForm(instance=mission)
    if request.method == 'POST':
        form = LaunchForm(request.POST, instance=mission)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'mission':mission,
        'form':form
    }
    return render(request,'accounts/launch_func.html',context)

def regRedirect(request):
    return render(request,'accounts/register_redirect.html')