"""
URL configuration for NoDot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from UserApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('schedule-pickup', views.schedule_pickup, name='schedule_pickup'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('services/<str:name>', views.servicedetails, name='servicedetails'),
    path('blogs', views.blogs, name='blogs'),
    path('contact', views.contact, name='contact'),
    path('careers', views.careers, name='careers'),
    path('careers/<str:title>', views.jobdetails, name='jobdetails'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('addservice', views.addservice, name='addservice'),
    path('delete_service/<int:service_id>', views.delete_service, name='delete_service'),
    path('jobpost', views.jobpost, name='jobpost'),
    # path('job/<int:job_id>/', views.job, name='jobdetails'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
