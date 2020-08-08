from django.db import models
from django.contrib.auth.models import User
import csv
# Create your models here.


class Customer(models.Model):

    customer_id = models.CharField("Customer ID",max_length=50, null=True)

    LOAN_STATUS = (
        ('a', 'Active'),
        ('r', 'Registered'),
        ('i', 'Inactive')
    )

    status = models.CharField(
        max_length=1, choices=LOAN_STATUS, blank=True, default='a', null=True)
    sys_access = models.BooleanField("System Access",default=False,null=True)
    zone = models.CharField(max_length=10, null=True)
    first_name = models.CharField(max_length=20, null=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)
    company_name = models.CharField("Company Name",max_length=200, null=True)
    mobile = models.CharField("Mobile Number",max_length=15, null=True, blank=True)
    line1 = models.CharField("Address Line 1",max_length=50, null=True)
    line2 = models.CharField("Address Line 2",max_length=50, null=True)
    line3 = models.CharField("Address Line 3",max_length=50, null=True)
    city = models.CharField(max_length=15, null=True)
    zip_code = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=50, null=True)
    date_created = models.DateField("Date Created",auto_now=True, null=True,blank=True)
    date_start = models.DateField("Date Started",auto_now=True, null=True,blank=True)
    date_end = models.DateField("Date Ended",auto_now_add=False, null=True,blank=True)

    def __str__(self):
        return f'{self.customer_id}'


class Location(models.Model):
    location_id = models.CharField(max_length=20, null=True)
    zone = models.CharField(max_length=10,null=True)
    station_name = models.CharField(max_length=100,null=True)
    manager = models.ManyToManyField(User)
    phone = models.CharField(max_length=15,null=True)
    email=models.CharField(max_length=30,null=True)
    line_1 = models.CharField(max_length=50,null=True)
    line_2 = models.CharField(max_length=50,null=True)
    line_3 = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=20,null=True,blank=True)
    zip_code  = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=70,null=True)
    area = models.CharField(max_length=150,null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    altitude = models.IntegerField(null=True)

    def __str__(self):
        return self.location_id


class Drone(models.Model):

    droneid = models.CharField("Drone ID",max_length=200, null=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1, choices=LOAN_STATUS, blank=True, default='m', null=True)
    locale = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL,verbose_name="Drone Station")
    make = models.CharField(max_length=100, null=True, blank=True)
    model_no = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    ean = models.CharField(max_length=10, null=True, blank=True)
    price_currency = models.CharField(max_length=3, blank=True, null=True)
    price = models.CharField(max_length=5, null=True, blank=False)
    warranty = models.CharField(max_length=10, null=True, blank=True)
    date_purchase = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    date_operation = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    date_shelved = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.droneid


class Mission(models.Model):

    def incrementid():
        no = Mission.objects.count()
        np = f'{no:06}'
        if no == None:
            return 'M000001'
        else:
            no = no+1
            np = f'M{no:06}'
            return np

    mission_id = models.CharField(
        max_length=10, null=True, default=incrementid, editable=False)
    date = models.DateField(auto_now_add=False, null=True)
    time = models.TimeField(auto_now_add=False,null=True)
    drone = models.ForeignKey(Drone, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    manager = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    MISSION_TYPE = (
        ('1', 'Loiter'),
        ('2', 'Circumferance'),
        ('3', 'Lawn-Mower'),
    )

    mission_type = models.CharField(
        max_length=10, choices=MISSION_TYPE, blank=True, default='2', null=True)

    INFO_TYPE = (
        ('1', 'Photo'),
        ('2', 'Video'),
    )
    mode_type = models.CharField(
        max_length=10, choices=INFO_TYPE, blank=True, default='1', null=True)

    STATE_TYPE = (
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
        ('Cancelled', 'Cancelled'),
        ('On Schedule','On Schedule')
    )
    mission_status = models.CharField(
        max_length=15, choices=STATE_TYPE, default='Pending', blank=True, null=True)

    LAUNCH_MODE = {
        ('AUTO', 'AUTO'),
        ('MANUAL', 'MANUAL')
    }
    launch_mode = models.CharField(
        max_length=7, choices=LAUNCH_MODE, default='MANUAL', null=True)
    mission_pic = models.ImageField(null=True, blank=True, default="logo.png",upload_to='mission_img')
    launch_now = models.BooleanField(null=True, default=False)

    def __str__(self):
        return str(self.mission_id)


class Launch(models.Model):

    mission = models.CharField(max_length=10, null=True)
    now = models.CharField(max_length=1, default='1', null=True)

    def __str__(self):
        return self.mission
