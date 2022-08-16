from statistics import mode
from django.db import models

# Create your models here.

class department(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sortindex=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name

class grade(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sortindex=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name

class lessons(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    grade=models.ForeignKey(grade,on_delete=models.CASCADE)
    sortindex=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name

class days(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class year(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class CourseType(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name