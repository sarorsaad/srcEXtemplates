from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
# from .models import Account
from .forms import AccountForm
########################

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


from django.contrib.auth import authenticate, login
from django.shortcuts import redirect




from django.contrib.auth import authenticate, login
from django.shortcuts import render

def loginpage(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        
        try:
            if user is not None:
                login(request, user)
                group_name = request.user.groups.all()[0].name
                
                if group_name == 'Doctor':
                    return render(request, 'doctor/doctor_dashboard.html')
        
        except Exception as e:
            print(e)
    
    return render(request, 'account/login.html')


 


##########################################################
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Doctor

def create_account(request):
    error = ""
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phonenumber = request.POST.get('phonenumber')
        birthdate = request.POST.get('birthdate')
        specialty = request.POST.get('specialty')
        rank = request.POST.get('rank')

        # Perform any necessary validation or processing with the form data
        
        try:
            if password == confirm_password:
                user = User.objects.create_user(
                    first_name=name,
                    email=email,
                    password=password,
                    username=username
                )
                doctor = Doctor.objects.create(
                    user=user,
                    name=name,
                    username=username,
                    email=email,
                    gender=gender,
                    phonenumber=phonenumber,
                    birthdate=birthdate,
                    specialty=specialty,
                    rank=rank
                )
                doc_group = Group.objects.get(name="Doctor")
                doc_group.user_set.add(user)
                error = "no"
            else:
                error = "yes"
        except Exception as e:
            error = "yes"

    d = {'error': error}
    return render(request, 'account/create_account.html', d)
################################


##################################

#############################

from django.contrib.auth import logout
from django.shortcuts import redirect

def Logout(request):
    logout(request)
    return redirect('loginpage')

class SendResettingMailView(View):
    template_name = 'account/Send resetting mail.html'

    def get(self, request):
        return render(request, self.template_name)






def admin_dashboard(request):
    return render(request, 'account/admin_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

def receptionist_dashboard(request):
    return render(request, 'receptionist_dashboard.html')

def radiologist_dashboard(request):
    return render(request, 'radiologist_dashboard.html')



################################################
##################################
def arabic_login(request):
    return render(request, 'account/arabicLogin.html')


def arabic_create_account(request):
    return render(request, 'account/arabic_create_account.html')

def arabic_send_resetting_mail(request):
    return render(request, 'account/arabic_Send resetting.html')




