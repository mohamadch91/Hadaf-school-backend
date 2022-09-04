
from django.db import models

from authen.models import Teacher
from course.models import Course

# Create your models here.

class quizHeader(models.Model):
    id=models.AutoField(primary_key=True)
    description=models.TextField(max_length=250,blank=True,null=True)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True,null=True)
    course=models.ForeignKey(Course,on_delete=models.Case,blank=True,null=True)
    quizTime=models.IntegerField( blank=True,null=True,default=0)
    start_data=models.DateTimeField(blank=True,null=True)
    end_data=models.DateTimeField(blank=True,null=True)
    question_count=models.IntegerField(blank=True,null=True,default=5)
    created_at=models.DateTimeField(auto_now_add=True,null=True)    ########
    updated_at=models.DateTimeField(auto_now=True,null=True) 

class quizQuestion(models.Model):
    id=models.AutoField(primary_key=True)
    header_id=models.ForeignKey(quizHeader,on_delete=models.CASCADE,blank=True,null=True)
    title=models.TextField(max_length=350,blank=True,null=True)
    answer1=models.TextField(max_length=400,blank=True,null=True)
    answer2=models.TextField(max_length=400,blank=True,null=True)
    answer3=models.TextField(max_length=400,blank=True,null=True)
    answer4=models.TextField(max_length=400,blank=True,null=True)
    result=models.IntegerField(blank=True,null=True)

class studentQueez(models.Model):
    id=models.AutoField(primary_key=True)
    quizheader=models.ForeignKey(quizHeader,on_delete=models.CASCADE,blank=True)    
    quizQuestion=models.ForeignKey(quizQuestion,on_delete=models.CASCADE,blank=True,null=True)
    result=models.IntegerField(blank=True,null=True)