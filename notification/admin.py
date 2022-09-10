from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(notification)
admin.site.register(studentNotification)
admin.site.register(studentNotificationRead)