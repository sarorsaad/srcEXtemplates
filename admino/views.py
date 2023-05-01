from django.shortcuts import render

def admin_dashboard(request):
    return render(request, 'admino/admin_dashboard.html')


def accounting(request):
    return render(request, 'admino/Accounting.html')


def activity_logs(request):
    return render(request, 'admino/ActivityLogs.html')



def backups(request):
    return render(request, 'admino/Backups.html')


def bookings(request):
    return render(request, 'admino/Bookings.html')


def contracts(request):
    return render(request, 'admino/Contracts.html')

def create_booking(request):
    return render(request, 'admino/CreateBooking.html')

def create_contract(request):
    return render(request, 'admino/CreateContract.html')

def create_doctor(request):
    return render(request, 'admino/CreateDoctor.html')

def create_invoice(request):
    return render(request, 'admino/CreateInvoice.html')

def create_patient(request):
    return render(request, 'admino/CreatePatient.html')

def create_role(request):
    return render(request, 'admino/CreateRole.html')

def create_test(request):
    return render(request, 'admino/CreateTest.html')

def create_user(request):
    return render(request, 'admino/CreateUser.html')

def doctor_report(request):
    # Add any necessary context data here
    context = {}
    return render(request, 'admino/DoctorReport.html', context)

def doctors(request):
    return render(request, 'admino/Doctors.html')

def edit_test(request):
    return render(request, 'admino/EditTest.html')
def expense_categories(request):
    return render(request, 'admino/ExpenseCategories.html')

def view_expenses(request):
    return render(request, 'admino/Expenses.html')

def view_invoices(request):
    return render(request, 'admino/Invoices.html')

def view_patients(request):
    return render(request, 'admino/Patients.html')

def view_profile(request):
    return render(request, 'admino/Profile.html')

def view_reports(request):
    return render(request, 'admino/Reports.html')

def roles(request):
    return render(request, 'admino/Roles.html')
def settings_view(request):
    return render(request, 'admino/Settings.html')

def tests_price_list(request):
    return render(request, 'admino/TestsPriceList.html')
def view_tests(request):
    return render(request, 'admino/Tests.html')
def translation(request):
    return render(request, 'admino/Translation.html')
def view_users(request):
    # Logic to retrieve and process user data goes here
    return render(request, 'admino/Users.html')