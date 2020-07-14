
from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='main-home'),
    path('about/', views.about, name='drone'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('statistics/', views.status, name='status'),
    path('mission/', views.mission, name='all-mission'),
    path('launch/<str:pk>/', views.launch, name='launch'),
    path('create_mission/', views.createMission, name='create-mission'),
    path('create_customer/', views.createCustomer, name='create-customer'),
    path('update_mission/<str:pk>', views.updateMission, name='update-mission'),
    path('update_customer/<str:pk>', views.updateCustomer, name='update-customer'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
]
