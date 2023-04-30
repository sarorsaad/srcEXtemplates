from django.urls import path
from .views import admin_dashboard
from . import views



app_name='admino'
urlpatterns = [
path('dashboard/', admin_dashboard, name='admin_dashboard'),
path('accounting/', views.accounting, name='accounting'),
path('activity-logs/', views.activity_logs, name='activity_logs'),
path('backups/', views.backups, name='backups'),
path('bookings/', views.bookings, name='bookings'),
path('contracts/', views.contracts, name='contracts'),
path('create-booking/', views.create_booking, name='create_booking'),
path('create-contract/', views.create_contract, name='create_contract'),
path('create-doctor/', views.create_doctor, name='create_doctor'),
path('create-invoice/', views.create_invoice, name='create_invoice'),
 path('create_patient/', views.create_patient, name='create_patient'),
 path('create-role/', views.create_role, name='create_role'),
 path('create-test/', views.create_test, name='create_test'),
path('create-user/', views.create_user, name='create_user'),
path('doctor-report/', views.doctor_report, name='doctor_report'),
 path('doctors/', views.doctors, name='doctors'),
 path('edit_test/', views.edit_test, name='edit_test'),
     path('expense_categories/', views.expense_categories, name='expense_categories'),
     path('expenses/', views.view_expenses, name='view_expenses'),
     path('invoices/', views.view_invoices, name='view_invoices'),
     path('patients/', views.view_patients, name='view_patients'),
     path('profile/', views.view_profile, name='view_profile'),
     path('reports/', views.view_reports, name='view_reports'),
     path('roles/', views.roles, name='roles'),
     path('settings/', views.settings_view, name='admino_settings'),
         path('tests-price-list/', views.tests_price_list, name='tests_price_list'),
          path('tests/', views.view_tests, name='view_tests'),
          path('translation/', views.translation, name='translation'),
          path('users/', views.view_users, name='view_users'),
]
