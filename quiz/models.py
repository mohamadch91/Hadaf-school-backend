from pydoc import describe
from pyexpat import model
from tkinter.messagebox import QUESTION
from turtle import title
from unittest import result
from django.db import models

from authen.models import Teacher
from course.models import Course

# Create your models here.

class quizHeader(models.Model):
    id=models.CharField(max_length=20,blank=True,null=True)
    description=models.TextField(max_length=250,blank=True,null=True)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True)
    course=models.ForeignKey(Course,on_delete=models.Case,blank=True)
    quizTime=models.IntegerField( blank=True,null=True,default=0)
    question_count=models.IntegerField(blank=True,null=True,default=5)
    created_at=models.DateTimeField(auto_now_add=True,null=True)    ########
    updated_at=models.DateTimeField(auto_now=True,null=True) 

class quizQuestion(models.Model):
    header_id=models.ForeignKey(quizHeader,on_delete=models.CASCADE,blank=True)
    title=models.TextField(max_length=350,blank=True,null=True)
    answer1=models.TextField(max_length=400,blank=True,null=True)
    answer2=models.TextField(max_length=400,blank=True,null=True)
    answer3=models.TextField(max_length=400,blank=True,null=True)
    answer4=models.TextField(max_length=400,blank=True,null=True)
    result=models.IntegerField(blank=True,null=True)

class studentQueez(models.Model):
    quizheader=models.ForeignKey(quizHeader,on_delete=models.CASCADE,blank=True)    
    quizQuestion=models.ForeignKey(quizQuestion,on_delete=models.CASCADE,blank=True)
    result=models.IntegerField(blank=True,null=True)