from django.db import models
from authen.models import Student
# Create your models here.

class basket(models.Model):
    id=models.AutoField(primary_key=True)
    studentID=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    type=models.CharField(max_length=50 ,choices=[('normal', 'normal'), ('timing', 'timing'), ('student', 'student'),('course','course')], null=True)
    buyID=models.IntegerField(blank=True, null=True)


class wallet(models.Model):
    id=models.AutoField(primary_key=True)
    studentID=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    amount=models.IntegerField(blank=True, null=True)
    date=models.DateField(null=True)    
