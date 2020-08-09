from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from functools import partial

DateInput = partial(forms.DateInput, {'class':'datepicker'})

class MissionForm(ModelForm):
    date = forms.DateField(widget = DateInput())
    class Meta:
        model = Mission
        fields = '__all__'
        exclude = ['vds','vda','vc']

class Mission2Form(ModelForm):
    date = forms.DateField(widget = DateInput())
    class Meta:
        model = Mission
        fields = '__all__'
        exclude = ['launch_now','vds','vda','vc']
        

class CustomerForm(ModelForm):
    date_end = forms.DateField(widget = DateInput(),required=False)

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['date_start','date_created']

class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class DroneForm(ModelForm):
    date_purchase = forms.DateField(widget = DateInput())
    date_operation = forms.DateField(widget = DateInput(),required=False)
    date_shelved = forms.DateField(widget = DateInput(),required=False)
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
        'locale': forms.TextInput(attrs={'disabled': 'true'}),
        'make': forms.TextInput(attrs={'disabled': 'true'}),
        'model_no': forms.TextInput(attrs={'disabled': 'true'}),
        'description': forms.TextInput(attrs={'disabled': 'true'}),
        'ean': forms.TextInput(attrs={'disabled': 'true'}),
        'price_currency': forms.TextInput(attrs={'disabled': 'true'}),
        'price': forms.TextInput(attrs={'disabled': 'true'}),
        'warranty': forms.TextInput(attrs={'disabled': 'true'}),
        'date_purchase': forms.TextInput(attrs={'disabled': 'true'}),
        'date_operation': forms.TextInput(attrs={'disabled': 'true'}),
        'date_shelved': forms.TextInput(attrs={'disabled': 'true'}),
    }

class LaunchForm(ModelForm):

    class Meta:
        model=Mission
        fields= ['launch_now']
