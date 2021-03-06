from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import MissionFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .decorators import unauthenticated_user
import csv
import io
from datetime import datetime


@login_required(login_url='login')
def home(request):
    customer = Customer.objects.values()[0:10]
    mission = Mission.objects.order_by('-mission_id').values()[0:10]
    context = {
        'customer': customer,
        'mission': mission,
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def about(request):
    dr = Drone.objects.values()
    return render(request, 'accounts/about.html', {'drones': dr})


@login_required(login_url='login')
def customer_list(request):
    customer = Customer.objects.values()
    context = {
        'customers': customer
    }
    return render(request, 'accounts/customer_list.html', context)


@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    mission = customer.mission_set.values().order_by('-mission_id')
    total_mission = mission.count()
    somedict = {'customer': customer, 'missions': mission,
                'total_mission': total_mission}
    return render(request, 'accounts/customer.html', somedict)


def is_valid(user):
    return user.groups.filter(name='Admin').exists()


@login_required(login_url='login')
def mission(request):
    #one_week_ago = datetime.today() - timedelta(days=7)
    #mission = Mission.objects.order_by('-mission_id')[0:50]
    mission = Mission.objects.order_by('mission_id').values()
    context = {
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
        form = Mission2Form(request.POST, request.FILES)
        #form2 = CoordinateForm(request.POST)
        if form.is_valid():  # and form2.is_valid():
            form.save()
            # print(form.cleaned_data['mission_id'])
            # form2.save()
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
        'mission_id': mission.mission_id,
    }
    return render(request, 'accounts/mission_update_form.html', context)


@login_required(login_url='login')
def status(request):
    customer = Customer.objects.all()
    mission = Mission.objects.all()
    context = {
        'customer': customer,
        'mission': mission,
        'total_missions': mission.count(),
        'total_drone': Drone.objects.all().count(),
        'maintenance_drone': Drone.objects.filter(status="m").count(),
        'onloan_drone': Drone.objects.filter(status="o").count(),
        'available_drone': Drone.objects.filter(status="a").count(),
        'reserved_drone': Drone.objects.filter(status="r").count(),
        'mission_complete': mission.filter(mission_status="Complete").count(),
        'mission_pending': mission.filter(mission_status="Pending").count(),
        'mission_cancelled': mission.filter(mission_status="Cancelled").count(),
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
    context = {'form': form,
               'customer': customer,

               }
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
            return redirect('drone')
    context = {
        'form': form,
    }
    return render(request, 'accounts/drone_form.html', context)


@login_required(login_url='login')
def updateDrone(request, pk):

    drone = Drone.objects.get(id=pk)
    form = DroneFormUpdate(instance=drone)
    if request.method == 'POST':
        form = DroneFormUpdate(request.POST, instance=drone)
        if form.is_valid():
            form.save()
            return redirect('drone')
    context = {'form': form, 'droneid': drone.droneid}
    return render(request, 'accounts/drone_form_update.html', context)


@login_required(login_url='login')
def mymission(request):

    mission = Mission.objects.all().filter(manager=request.user)
    context = {
        'missions': mission,
    }
    return render(request, 'accounts/mymission.html', context)


@login_required(login_url='login')
def my_drone(request, pk):

    drone = Drone.objects.get(id=pk)
    drone_info = drone.mission_set.values()
    form = MyDroneForm(instance=drone)
    context = {
        'drone': drone,
        'drone_info': drone_info,
        'form': form,
    }
    return render(request, 'accounts/my_drone.html', context)


@login_required(login_url='login')
def launch_drone(request, pk):
    mission = Mission.objects.get(id=pk)
    form = LaunchForm(instance=mission)
    if request.method == 'POST':
        form = LaunchForm(request.POST, instance=mission)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'mission': mission,
        'form': form
    }
    return render(request, 'accounts/launch_func.html', context)


def regRedirect(request):
    return render(request, 'accounts/register_redirect.html')


@login_required(login_url='login')
def testing(request):

    if (request.method == 'GET'):
        return render(request, 'accounts/test.html')

    csv_file = request.FILES['file']

    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)
    for row in csv.reader(io_string):
        print(row[0])
        create_me = Mission.objects.create(
            mission_id=row[0],
            state=Location.objects.get(location_id=row[1]),
            drone=Drone.objects.get(droneid=row[2]),
            mission_type=row[3],
            date=row[4],
            time=row[5],
            mission_status=row[6],
            launch_mode=row[7],
            customer=Customer.objects.get(customer_id=row[8])


        )
    return render(request, 'accounts/test.html')
