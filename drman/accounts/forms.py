from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class MissionForm(ModelForm):
    class Meta:
        model = Mission
        fields = '__all__'

class Mission2Form(ModelForm):
    class Meta:
        model = Mission
        fields = '__all__'
        exclude = ['launch_now']
        

class CustomerForm(ModelForm):
    
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['date_start','date_end','date_created']

class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class DroneForm(ModelForm):
    class Meta:
        model = Drone
        fields = '__all__'

class MyDroneForm(ModelForm):
    class Meta:
        model = Drone
        fields = '__all__'
        widgets = {
        'droneid': forms.TextInput(attrs={'disabled': 'true'}),
        'status': forms.TextInput(attrs={'disabled': 'true'}),
    }

class LaunchForm(ModelForm):

    class Meta:
        model=Mission
        fields= ['launch_now']
