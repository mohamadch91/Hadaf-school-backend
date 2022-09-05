from django.db import models
from course.models import Course
from authen.models import Student
# Create your models here.


class normalPackage(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, blank=True, null=True)
    percent=models.IntegerField(blank=True, null=True)

class normalPackageCourse(models.Model):
    id=models.AutoField(primary_key=True)
    packageID=models.ForeignKey(normalPackage, on_delete=models.CASCADE, null=True)
    courseID=models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

class timingPackage(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, blank=True, null=True)
    percent=models.IntegerField(blank=True, null=True)
    asDate=models.DateField(null=True)
    toDate=models.DateField(null=True)

class timingPackageCourse(models.Model):
    id=models.AutoField(primary_key=True)
    packageID=models.ForeignKey(timingPackage, on_delete=models.CASCADE, null=True)
    courseID=models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

class studentPackage(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, blank=True, null=True)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

class studentPackageCourse(models.Model):
    id=models.AutoField(primary_key=True)
    packageID=models.ForeignKey(studentPackage, on_delete=models.CASCADE, null=True)
    courseID=models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

class studentPackageDiscount(models.Model):
    id=models.AutoField(primary_key=True)
    percent=models.IntegerField(blank=True, null=True)
    max_count=models.IntegerField(blank=True, null=True)