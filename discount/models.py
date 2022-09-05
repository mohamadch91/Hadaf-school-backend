from unicodedata import name
from django.db import models
from course.models import   Course
from authen.models import User
# Create your models here.
class Discount(models.Model):
    id  = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    asDate = models.DateField(null=True)    #####
    toDate = models.DateField(null=True)    ######
    amount = models.IntegerField(blank=True, null=True)
    isPercent = models.BooleanField(default=True,null=True)
    active = models.BooleanField(default=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True) #####
    updated_at=models.DateTimeField(auto_now=True,null=True)    ####  


class DiscountCourse(models.Model): #???????
    id = models.AutoField(primary_key=True)
    discountID = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

class DiscountUser(models.Model): #???????
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, blank=True, null=True)
    family=models.CharField(max_length=50, blank=True, null=True)
    phone=models.CharField(max_length=50, blank=True, null=True)
    code=models.CharField(max_length=50, blank=True, null=True)
    percent=models.IntegerField(blank=True, null=True)