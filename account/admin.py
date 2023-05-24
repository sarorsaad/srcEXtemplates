from django.contrib import admin
# from .models import Account

# admin.site.register(Account)


from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'gender', 'phonenumber', 'birthdate', 'specialty', 'rank')
    list_filter = ('specialty', 'rank', 'gender')
    search_fields = ('name', 'username', 'email', 'phonenumber')
    # Add any additional configuration or customization as needed

admin.site.register(Doctor, DoctorAdmin)
