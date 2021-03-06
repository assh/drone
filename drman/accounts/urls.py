
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [

    path('', views.home, name='main-home'),
    path('about/', views.about, name='drone'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('statistics/', views.status, name='status'),
    path('customer_list/', views.customer_list, name='customer-list'),
    path('mission/', views.mission, name='all-mission'),
    path('launch/<str:pk>/', views.launch, name='launch'),
    path('create_mission/', views.createMission, name='create-mission'),
    path('create_customer/', views.createCustomer, name='create-customer'),
    path('update_mission/<str:pk>', views.updateMission, name='update-mission'),
    path('update_customer/<str:pk>', views.updateCustomer, name='update-customer'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('testing/', views.testing, name='testing'),
    path('reg_redirect/', views.regRedirect, name='register-redirect'),
    path('create_drone/', views.createDrone, name='create-drone'),
    path('update_drone/<str:pk>', views.updateDrone, name='update-drone'),
    path('my_mission/', views.mymission, name='my-mission'),
    path('my_drone/<str:pk>', views.my_drone, name='my-drone'),
    path('launch_drone/<str:pk>', views.launch_drone, name='launch-drone'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_complete'),
]
