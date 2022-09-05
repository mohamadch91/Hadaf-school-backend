from django.contrib import admin

# Register your models here.
from . models import *
admin.site.register(Discount)
admin.site.register(DiscountCourse)
admin.site.register(DiscountUser)
