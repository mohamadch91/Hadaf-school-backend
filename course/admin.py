from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Course)
admin.site.register(StudetCourse)

admin.site.register(CourseHomeWork)

admin.site.register(CourseDays)
admin.site.register(CourseType)
