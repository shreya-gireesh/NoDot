from django import forms
from UserApp.models import *

class YourFormClass(forms.Form):
    mobileNumber = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    pickup_date = forms.DateField(required=True)
    pickup_time = forms.TimeField(required=True)

class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        fields = ['service_name', 'description', 'images']
        widgets = {
            'serivce_name': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Service Name'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'images': forms.FileInput(attrs={'class': 'form-file'}),
        }

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPostModel
        fields = [
            'title', 'description', 'responsibilities', 'requirements',
            'desirable_skills', 'education', 'job_type', 'location', 'experience_required'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'class': 'quill-editor'}),
            'responsibilities': forms.Textarea(attrs={'class': 'quill-editor'}),
            'requirements': forms.Textarea(attrs={'class': 'quill-editor'}),
            'desirable_skills': forms.Textarea(attrs={'class': 'quill-editor'}),
        }

class ApplyForm(forms.ModelForm):
    class Meta:
        model = JobApplyModel
        fields =[
            'name', 'email', 'phone_no', 'resume'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email'}),
            'phone_no':forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Phone Number'}),
            'resume': forms.FileInput(attrs={'class': 'form-file'}),
        }