from datetime import datetime
from dbm import error

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from NoDot.asgi import application
from UserApp.forms import *
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

def about(request):
    return render(request, 'about.html')

def services(request):
    services = ServiceModel.objects.all()
    return render(request, 'service.html', {'services': services})

def blogs(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def careers(request):
    jobs = JobPostModel.objects.all()
    return render(request, 'careers.html', {'jobs': jobs})

def jobdetails(request, title):
    date = datetime.now()
    job = JobPostModel.objects.get(title = title)
    if request.method == 'POST':

        job_detail = request.POST.get('job-detail')
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = JobPostModel.objects.get(job_id = job_detail)
            application.created_at = date
            application.save()
            messages.success(request, 'Your application has been submitted successfully!')
            form = ApplyForm()
    else:
        form = ApplyForm()

    return render(request, 'job-details.html', {'form': form, 'job': job})

def servicedetails(request, name):
    service = ServiceModel.objects.get(service_name=name)
    return render(request, 'service-details.html',{'service':service})


# admin
def dashboard(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')

    admin = AdminModel.objects.get(admin_id=user)

    admin_name = admin.admin_name
    pickups = PickupModel.objects.all()
    pickup_counts = pickups.count()
    return render(request, 'dashboard.html', {'pickups': pickups, 'total_pickup': pickup_counts, 'username': admin_name})

def addservice(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')

    admin = AdminModel.objects.get(admin_id=user)

    admin_name = admin.admin_name
    services = ServiceModel.objects.all()
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Service created successfully!')
            form.save()
            return redirect('addservice')  # Redirect to a relevant page after submission
    else:
        form = ServiceForm()
    return render(request, 'addservice.html', {'form': form, 'services': services, 'username': admin_name})

def delete_service(request, service_id):
    service = get_object_or_404(ServiceModel, pk=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('addservice')  # Adjust the redirect based on your URL name for the user list page
    return redirect('addservice')

def jobpost(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')

    admin = AdminModel.objects.get(admin_id=user)

    admin_name = admin.admin_name
    date = datetime.now()
    if request.method == 'POST':
        # Fetch data from POST request
        title = request.POST.get('title')
        description = request.POST.get('description')  # This contains HTML
        responsibilities = request.POST.get('responsibilities')  # Contains HTML
        requirements = request.POST.get('requirements')  # Contains HTML
        desirable_skills = request.POST.get('desirable_skills')  # Contains HTML
        education = request.POST.get('education')
        job_type = request.POST.get('job_type')
        location = request.POST.get('location')
        experience_required = request.POST.get('experience_required')

        if title and description:
            job_post = JobPostModel(
                title=title,
                description=description,  # HTML with bullet points retained
                responsibilities=responsibilities,  # HTML with bullet points retained
                requirements=requirements,  # HTML with bullet points retained
                desirable_skills=desirable_skills,  # HTML with bullet points retained
                education=education,
                job_type=job_type,
                location=location,
                experience_required=experience_required,
                created_at = date
            )
            job_post.save()
    return render(request, 'jobpost.html', {'username': admin_name})

def job(request, job_id):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')

    admin = AdminModel.objects.get(admin_id=user)

    admin_name = admin.admin_name
    job_post = JobPostModel.objects.get(job_id=job_id)
    return render(request, 'job.html', {'job_post': job_post, 'username': admin_name})