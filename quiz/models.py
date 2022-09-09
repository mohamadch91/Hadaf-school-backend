
from django.db import models

from authen.models import Student, Teacher
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
    min_range=models.IntegerField(blank=True,null=True,default=5)
    type=models.CharField(max_length=50,blank=True,null=True)
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
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    result=models.IntegerField(blank=True,null=True)


class totalquizHeader(models.Model):
    id=models.AutoField(primary_key=True)
    description=models.TextField(max_length=250,blank=True,null=True)
    quizTime=models.IntegerField( blank=True,null=True,default=0)
    question_count=models.IntegerField(blank=True,null=True,default=5)
    created_at=models.DateTimeField(auto_now_add=True,null=True) 
    start_data=models.DateTimeField(blank=True,null=True)
    end_data=models.DateTimeField(blank=True,null=True)   ########
    updated_at=models.DateTimeField(auto_now=True,null=True)

class totalquizSubjects(models.Model):
    id=models.AutoField(primary_key=True)
    quizheader=models.ForeignKey(totalquizHeader,on_delete=models.CASCADE,blank=True,null=True)
    subject=models.CharField(max_length=50,blank=True,null=True)
    ratio=models.IntegerField(blank=True,null=True,default=0)
    created_at=models.DateTimeField(auto_now_add=True,null=True)    ########
    updated_at=models.DateTimeField(auto_now=True,null=True)

class totalquizQuestion(models.Model):
    id=models.AutoField(primary_key=True)
    header_id=models.ForeignKey(totalquizHeader,on_delete=models.CASCADE,blank=True,null=True)
    #quiz subject
    subject=models.ForeignKey(totalquizSubjects,on_delete=models.CASCADE,blank=True,null=True)
    title=models.TextField(max_length=350,blank=True,null=True)
    answer1=models.TextField(max_length=400,blank=True,null=True)
    answer2=models.TextField(max_length=400,blank=True,null=True)
    answer3=models.TextField(max_length=400,blank=True,null=True)
    answer4=models.TextField(max_length=400,blank=True,null=True)
    result=models.IntegerField(blank=True,null=True)

class totalstudentQueez(models.Model):
    id=models.AutoField(primary_key=True)
    quizheader=models.ForeignKey(totalquizHeader,on_delete=models.CASCADE,blank=True)    
    quizQuestion=models.ForeignKey(totalquizQuestion,on_delete=models.CASCADE,blank=True,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    result=models.IntegerField(blank=True,null=True)