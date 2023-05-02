from django.shortcuts import render

def doctor_dashboard(request):
    # Your view code here
    return render(request, 'doctor/doctor_dashboard.html', context={})




def booking(request):
    return render(request, 'doctor/Booking.html')


def view_profile(request):
    return render(request, 'doctor/Profile.html')



def reports(request):
    return render(request, 'doctor/Reports.html')


def tests_library(request):
    return render(request, 'doctor/Tests Library.html')

