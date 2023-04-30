from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Doctor', 'Doctor'),
        ('Receptionist', 'Receptionist'),
        ('Technicians', 'Technicians'),
        ('Radiologist', 'Radiologist'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.role}"
