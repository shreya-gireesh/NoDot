from datetime import datetime
from dbm import error

from django.shortcuts import render, redirect
from UserApp.forms import YourFormClass
from UserApp.models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def schedule_pickup(request):
    today = datetime.now()
    if request.method == 'POST':


        # You can create a form instance using the POST data
        form = YourFormClass(request.POST)

        if form.is_valid():
            # Access cleaned data
            mobile_number = form.cleaned_data['mobileNumber']
            address = form.cleaned_data['address']
            pickup_date = form.cleaned_data['pickup_date']
            pickup_time = form.cleaned_data['pickup_time']

            # Here you can save the data to the database or perform other logic
            # For example:
            PickupModel.objects.create(mobile_no=mobile_number, address=address,
                                     pickup_date=pickup_date, pickup_time=pickup_time, created_at = today)

            # Redirect to a success page or another view
            # Update with your success URL
            return redirect('schedule_pickup')

    else:
        # If the request is GET, initialize an empty form
        form = YourFormClass()

    return render(request, 'shedule-pickup.html', {'form': form})

def dashboard(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')

    admin = AdminModel.objects.get(admin_id=user)

    admin_name = admin.admin_name
    pickups = PickupModel.objects.all()
    pickup_counts = pickups.count()
    return render(request, 'dashboard.html', {'pickups': pickups, 'total_pickup': pickup_counts, 'username': admin_name})

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def login(request):
    error = None
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')

        try:
            admin = AdminModel.objects.get(admin_mail=identifier, admin_password=password)
            request.session['user'] = admin.admin_id
            request.session.set_expiry(90)
            return redirect('dashboard')
        except AdminModel.DoesNotExist:
            error = "User doesnt exist"

    return render(request, 'login.html', {'error': error})