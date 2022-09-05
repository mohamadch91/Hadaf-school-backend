from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(normalPackage)
admin.site.register(normalPackageCourse)
admin.site.register(timingPackage)
admin.site.register(timingPackageCourse)
admin.site.register(studentPackage)
admin.site.register(studentPackageCourse)
admin.site.register(studentPackageDiscount)