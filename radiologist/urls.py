from django.urls import path
from . import views

app_name = 'radiologist'

urlpatterns = [
    path('radiologist/dashboard/', views.radiologist_dashboard, 
         name='radiologist_dashboard'),
    
    path('booking/', views.booking, name='booking'),
    
    path('profile/', views.view_profile, name='radiologist_profile'),
    
    path('reports/', views.reports, name='reports'),
    
     path('tests-library/', views.tests_library, name='tests_library'),
]
    

