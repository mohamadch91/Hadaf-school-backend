from venv import create
from django.db import models

# Create your models here.
class buy(models.Model):
    student=models.ForeignKey('authen.Student',on_delete=models.CASCADE)
    amount=models.IntegerField()
    authority=models.CharField(max_length=200)
    url=models.CharField(max_length=200,null=True)
    type=models.CharField(max_length=200,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)