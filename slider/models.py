from django.db import models

# Create your models here.
class Slider(models.Model):
    id=models.AutoField(primary_key=True)
    picture=models.ImageField(upload_to='slider/',null=True,blank=True)
    link=models.CharField(max_length=255,blank=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,blank=True)

class Banner(models.Model):
    id=models.AutoField(primary_key=True)
    picture=models.ImageField(upload_to='banner/',null=True,blank=True)
    title=models.CharField(max_length=255,blank=True,null=True)
    active=models.BooleanField(default=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)    