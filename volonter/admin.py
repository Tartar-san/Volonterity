from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Cities)
admin.site.register(ActivityTypes)
admin.site.register(Organization)
admin.site.register(OrganizationProfile)
admin.site.register(OrganizationImages)
admin.site.register(Event)
admin.site.register(EventTimes)
admin.site.register(EventImages)