from django.contrib import admin
from UserApp.models import *

# Register your models here.
admin.site.register(AdminModel)
admin.site.register(PickupModel)
admin.site.register(ServiceModel)
admin.site.register(JobPostModel)
admin.site.register(JobApplyModel)