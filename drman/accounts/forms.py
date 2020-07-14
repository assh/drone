from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class MissionForm(ModelForm):

    class Meta:
        model = Mission
        fields = '__all__'

class CustomerForm(ModelForm):
    
    class Meta:
        model = Customer
        fields = '__all__'

class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
