from django.urls import path
from . import views

app_name = 'receptionist'

urlpatterns = [
    path('receptionist/dashboard/', views.receptionist_dashboard, name='receptionist_dashboard'),
]
