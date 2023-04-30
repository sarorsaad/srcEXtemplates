from django.urls import path
from . import views

app_name = 'radiologist'

urlpatterns = [
    path('radiologist/dashboard/', views.radiologist_dashboard, name='radiologist_dashboard'),
]
