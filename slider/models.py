from django.db import models

# Create your models here.
class Slider(models.Model):
    id=models.AutoField(primary_key=True)
    picture=models.ImageField(upload_to='slider/')
    link=models.CharField(max_length=255)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Banner(models.Model):
    id=models.AutoField(primary_key=True)
    picture=models.ImageField(upload_to='banner/')
    title=models.CharField(max_length=255)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)    