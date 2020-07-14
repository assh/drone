from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MissionForm(ModelForm):

    class Meta:
        model = Mission
        fields = '__all__'

class CustomerForm(ModelForm):
    
    class Meta:
        model = Customer
        fields = '__all__'

