from django import forms

class AccountForm(forms.Form):
    name = forms.CharField(max_length=50)
    role = forms.CharField(widget=forms.RadioSelect(choices=[('Admin', 'Admin'), ('Doctor', 'Doctor'), ('Receptionist', 'Receptionist'), ('Technicians', 'Technicians'), ('Radiologist', 'Radiologist')]))
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

