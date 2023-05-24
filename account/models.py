from django.db import models

# class Account(models.Model):
#     name = models.CharField(max_length=100)
#     ROLE_CHOICES = [
#         ('Admin', 'Admin'),
#         ('Doctor', 'Doctor'),
#         ('Receptionist', 'Receptionist'),
#         ('Technicians', 'Technicians'),
#         ('Radiologist', 'Radiologist'),
#     ]
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.name} - {self.role}"

###################################
####################

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields if needed
    email = models.EmailField(unique=True)
    
    # Define related_name for groups and user_permissions fields
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')

    def __str__(self):
        return self.username



from django.contrib import admin
from django.db import models

class Doctor(models.Model):
    SPECIALTY_CHOICES = [
        ('IMC', 'IMC'),
        ('Surgery', 'Surgery'),
        ('OBG', 'OBG'),
        ('Pedia', 'Pedia'),
        ('Ortho', 'Ortho'),
        ('Nepherology', 'Nepherology'),
        # Add more choices as needed
    ]

    RANK_CHOICES = [
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Consultant', 'Consultant'),
        ('Associate Professor', 'Associate Professor'),
        ('Registrar', 'Registrar'),
        ('Senior Registrar', 'Senior Registrar'),
        ('Specialist', 'Specialist'),
        # Add more choices as needed
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default='default_username')
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Other')
    phonenumber = models.CharField(max_length=10)
    birthdate = models.DateField()
    specialty = models.CharField(max_length=50, choices=SPECIALTY_CHOICES)
    rank = models.CharField(max_length=50, choices=RANK_CHOICES, default='Junior')

    def __str__(self):
        return self.name  # Customize how the instance is displayed




