from django import forms

class YourFormClass(forms.Form):
    mobileNumber = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    pickup_date = forms.DateField(required=True)
    pickup_time = forms.TimeField(required=True)