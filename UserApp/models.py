from django.db import models

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