from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from .models import Account
from .forms import AccountForm


class LoginBaseView(View):
    template_name = 'account/LoginBase.html'

    def get(self, request):
        return render(request, self.template_name)

def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            # Process the form data as needed
            # For example, create a new user account using the data
            name = form.cleaned_data['name']
            role = form.cleaned_data['role']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            # Create a new user account using the data
            # ...
            # Redirect the user to a success page or to their new account page
            return render(request, 'account/success.html')
    else:
        form = AccountForm()
    return render(request, 'account/create_account.html', {'form': form})

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