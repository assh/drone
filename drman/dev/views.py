from django.shortcuts import render,HttpResponse
import csv
import io
from accounts.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def mission_upload(request):

    if (request.method == 'GET'):
        return render(request, 'dev/mission_upload.html')

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
    return render(request, 'dev/mission_upload.html')