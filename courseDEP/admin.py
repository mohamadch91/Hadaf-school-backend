from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(department)
admin.site.register(grade)
admin.site.register(lessons)
admin.site.register(days)
admin.site.register(year)
admin.site.register(CourseType)