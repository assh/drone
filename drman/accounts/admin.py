from django.contrib import admin
from .models import Customer,Drone,Mission
# Register your models here.

admin.site.register(Customer)
admin.site.register(Drone)
admin.site.register(Mission)