from django.shortcuts import render

def radiologist_dashboard(request):
    return render(request, 'radiologist/radiologist_dashboard.html')

def booking(request):
    return render(request, 'radiologist/Booking.html')


def view_profile(request):
    return render(request, 'radiologist/Profile.html')



def reports(request):
    return render(request, 'radiologist/Reports.html')


def tests_library(request):
    return render(request, 'radiologist/Tests Library.html')
