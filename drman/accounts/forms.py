from django.forms import ModelForm
from .models import *

class MissionForm(ModelForm):

    class Meta:
        model = Mission
        fields = '__all__'