from django.urls import path
from .views import *

urlpatterns = [
    path('mission/',mission_upload,name="mission-upload"),
]