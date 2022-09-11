
from django.db import models

from courseDEP.models import *
from authen.models import *



class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100,null=True)
    picture1 = models.ImageField(upload_to='course_pictures/',blank=True,null=True)
    picture2 = models.ImageField(upload_to='course_pictures/',blank=True,null=True)
    departmentID = models.ForeignKey(department,on_delete=models.CASCADE,null=True)
    gradeID = models.ForeignKey(grade,on_delete=models.CASCADE,null=True)
    teacherID = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True, related_name='Teacher')
    courseTypeID = models.ForeignKey(CourseType,on_delete=models.CASCADE,null=True)
    lessonID = models.ForeignKey(lessons,on_delete=models.CASCADE,null=True)
    yearID = models.ForeignKey(year,on_delete=models.CASCADE,null=True)
    price1 = models.IntegerField(blank=True, null=True)
    price2 = models.IntegerField(blank=True, null=True)
    returnPercent = models.IntegerField(blank=True, null=True)
    day = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=500,null=True)
    startTime = models.DateField(null=True)
    showforstudents = models.BooleanField(default=True,null=True)
    showforTeacher = models.BooleanField(default=True ,null=True)
    enableforbuy = models.BooleanField(default=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    end = models.BooleanField(default=True,null=True)
    endDateTime = models.DateField(null=True)
    active = models.BooleanField(default=True,null=True)
    userID = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='User')


class StudetCourse(models.Model):
    id = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, null=True) 
    price = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=500,null=True)
    enable = models.BooleanField(default=True,null=True)  #########
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

class BlocedStudent(models.Model):
    id = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)


class CourseHomeWork(models.Model):
    id = models.AutoField(primary_key=True)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    fileCourse = models.FileField(upload_to ='upload_course/', max_length=100, null=True,blank=True) 
    endDateTime = models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    active = models.BooleanField(default=True, null=True)

class Homeworkanswer(models.Model):
    id=models.AutoField(primary_key=True)
    courseHWID=models.ForeignKey(CourseHomeWork,on_delete=models.CASCADE,null=True)
    file=models.FileField(upload_to ='hw_answer/', max_length=100, null=True,blank=True)
    studentID=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)


class CourseDays(models.Model):        #???????????
    id = models.AutoField(primary_key=True)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    dayID = models.ForeignKey(days,on_delete=models.CASCADE, null=True)     #######
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

class CourseType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    sortIndex = models.IntegerField(blank=True, null=True)    ########  ????????
    created_at=models.DateTimeField(auto_now_add=True,null=True)    ########
    updated_at=models.DateTimeField(auto_now=True,null=True)    #######


