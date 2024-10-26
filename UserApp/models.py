from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class AdminModel(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100)
    admin_mail = models.EmailField()
    admin_password = models.CharField(max_length=100)

    def __str__(self):
        return self.admin_name

class PickupModel(models.Model):
    pickup_id = models.AutoField(primary_key = True)
    mobile_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.mobile_no

class ServiceModel(models.Model):
    service_id = models.AutoField(primary_key = True)
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.FileField(upload_to='services/')

    def __str__(self):
        return self.service_name

class JobPostModel(models.Model):
    job_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    responsibilities = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    desirable_skills = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    job_type = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255)
    experience_required = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class JobApplyModel(models.Model):
    apply_id = models.AutoField(primary_key = True)
    job = models.ForeignKey(JobPostModel, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
