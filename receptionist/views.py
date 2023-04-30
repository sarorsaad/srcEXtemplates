from django.shortcuts import render

def receptionist_dashboard(request):
    return render(request, 'receptionist/receptionist_dashboard.html')
