from django.shortcuts import render

def doctor_dashboard(request):
    # Your view code here
    return render(request, 'doctor/doctor_dashboard.html', context={})
