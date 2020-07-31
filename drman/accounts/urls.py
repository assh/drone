
from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('logout/', views.logoutUser, name='logout'),
    path('create_drone/', views.createDrone, name='create-drone'),
    path('update_drone/<str:pk>', views.updateDrone, name='update-drone'),
    path('my_mission/', views.mymission, name='my-mission'),
    path('my_drone/<str:pk>', views.my_drone, name='my-drone'),
    path('launch_drone/<str:pk>', views.launch_drone, name='launch-drone'),

    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
