from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Location(models.Model):
    location_id = models.CharField(max_length=20, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    altitude = models.IntegerField(null=True)

    def __str__(self):
        return self.location_id


class Drone(models.Model):

    droneid = models.CharField(max_length=200, null=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1, choices=LOAN_STATUS, blank=True, default='m', null=True)
    locale = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)

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

    mission_id = models.CharField(max_length=10, null=True,default = incrementid,editable=False)
    date_future = models.DateTimeField(auto_now_add=False, null=True)
    drone = models.ForeignKey(Drone, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    manager = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    MISSION_TYPE = (
        ('1', 'Loiter'),
        ('2', 'Circumferance'),
        ('3', 'Lawn-Mower'),
    )

    mission_type = models.CharField(
        max_length=1, choices=MISSION_TYPE, blank=True, default='2', null=True)

    INFO_TYPE = (
        ('1', 'Photo'),
        ('2', 'Video'),
    )
    mode_type = models.CharField(
        max_length=1, choices=INFO_TYPE, blank=True, default='1', null=True)

    STATE_TYPE = (
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
        ('Cancelled', 'Cancelled')
    )
    mission_status = models.CharField(
        max_length=10, choices=STATE_TYPE, default='Pending', blank=True, null=True)

    

    def __str__(self):
        return self.mission_id
