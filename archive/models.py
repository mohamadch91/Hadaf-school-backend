from django.db import models
from course.models import Course
# class archiveOfflineHeader(models.Model):
class ArchiveOfflineHeader(models.Model):
    id = models.AutoField(primary_key=True)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

class ArchiveFiles(models.Model):
    id = models.AutoField(primary_key=True)
    archiveHeaderID = models.ForeignKey(ArchiveOfflineHeader, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    fileArchibe = models.FileField(upload_to ='upload_course/', max_length=100, null=True,blank=True)
    reated_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
