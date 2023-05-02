from django.urls import path
from . import views
from .views import create_account
from .views import admin_dashboard  # replace with your view function name



app_name='account'
urlpatterns = [
    path('', views.LoginBaseView.as_view(), name='login_base'),
     path('create-account/', create_account, name='create_account'),
    path('send_resetting_mail/', views.SendResettingMailView.as_view(), name='send_resetting_mail'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('receptionist_dashboard/', views.receptionist_dashboard, name='receptionist_dashboard'),
    path('radiologist_dashboard/', views.radiologist_dashboard, name='radiologist_dashboard'),
   #################################
   #######################
    path('arabic-login/', views.arabic_login, name='arabic_login'),
    path('arabic/create-account/', 
             views.arabic_create_account, name='arabic_create_account'), 
     path('arabic/send-resetting-mail/', views.arabic_send_resetting_mail, 
          name='arabic_send_resetting_mail'),
]
