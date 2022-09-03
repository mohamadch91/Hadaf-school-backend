
from django.db import models
from authen.models import Student, Teacher, User
from course.models import Course
# Create your models here.

class ForumHeader(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(max_length=250,blank=True,null=True)
    picture=models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    Userid= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at=models.DateField(auto_now_add=True,blank=True,null=True)
    updated_at=models.DateField(auto_now=True,blank=True,null=True)

    
class ForumDetail(models.Model):
    id=models.AutoField(primary_key=True)
    ForumHeaderid=models.ForeignKey(ForumHeader,on_delete=models.CASCADE, null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,related_name='student')
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True,related_name='teacher')
    show=models.BooleanField(default=True)
    title=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(max_length=250,blank=True,null=True)
    file=models.FileField(upload_to='forum_file/',blank=True,null=True)
    created_at=models.DateField(auto_now_add=True,blank=True,null=True)
    updated_at=models.DateField(auto_now=True,blank=True,null=True)

