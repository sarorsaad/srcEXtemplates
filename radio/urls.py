from django.urls import path
from . import views


app_name='radio'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    # Other URL patterns for your app
]
