from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Drone)
admin.site.register(Mission)
admin.site.register(Location)
admin.site.register(Launch)
#admin.site.register(CSVFileFolder)