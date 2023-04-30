from django.shortcuts import render

def radiologist_dashboard(request):
    return render(request, 'radiologist/radiologist_dashboard.html')
