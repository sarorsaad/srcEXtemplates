from django.urls import path
from . import views




app_name='doctor'
urlpatterns = [
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    # other URL patterns...
    path('booking/', views.booking, name='booking'),
    
    path('profile/', views.view_profile, name='doctor_profile'),
    
    path('reports/', views.reports, name='reports'),
    
     path('tests-library/', views.tests_library, name='tests_library'),
]
