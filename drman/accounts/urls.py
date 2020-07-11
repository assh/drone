
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='main-home'),
    path('about/', views.about,name='drone'),
    path('customer/<str:pk>/', views.customer,name='customer'),
    path('mission/',views.mission,name='all-mission'),
]
