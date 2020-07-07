from django.db import models

# Create your models here.

class Customer(models.Model):


    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return f'{self.name}'

class Drone(models.Model):

    droneid = models.CharField(max_length=200,null=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m',null=True)
    station = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.droneid

class Mission(models.Model):
    mission_id = models.CharField(max_length=10,null=True)
    date_future = models.DateTimeField(auto_now_add=False,null=True)
    drone = models.OneToOneField(Drone,null=True,on_delete=models.SET_NULL)
    customer = models.OneToOneField(Customer,null=True,on_delete=models.SET_NULL)
    MISSION_TYPE = (
        ('1', 'Loiter'),
        ('2', 'Circumferance'),
        ('3', 'Lawn-Mower'),
    )

    mission_type = models.CharField(max_length=1,choices=MISSION_TYPE,blank=True,default='2',null=True)

    INFO_TYPE = (
        ('1', 'Photo'),
        ('2', 'Video'),
    )
    mode_type = models.CharField(max_length=1,choices=INFO_TYPE,blank=True,default='1',null=True)

    def __str__(self):
        return self.mission_type

class Location(models.Model):
    location_id = models.CharField(max_length=20,null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    altitude = models.IntegerField(null=True)
    drone = models.ForeignKey(Drone,null=True,on_delete=models.SET_NULL)
