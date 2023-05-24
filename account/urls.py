from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('create-account/', views.create_account, name='create_account'),
    path('send_resetting_mail/', views.SendResettingMailView.as_view(), name='send_resetting_mail'),
    
    path('arabic-login/', views.arabic_login, name='arabic_login'),
    path('arabic/create-account/', views.arabic_create_account, name='arabic_create_account'),
    path('arabic/send-resetting-mail/', views.arabic_send_resetting_mail, name='arabic_send_resetting_mail'),
]