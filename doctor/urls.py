from django.urls import path
from . import views




app_name='doctor'
urlpatterns = [
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    # other URL patterns...
]
