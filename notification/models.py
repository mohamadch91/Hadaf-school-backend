from django.db import models
from authen.models import Student
# Create your models here.
class notification(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(max_length=250,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.title

class studentNotification(models.Model):
    id=models.AutoField(primary_key=True)
    notification=models.ForeignKey(notification,on_delete=models.CASCADE,blank=True,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return str(self.id)