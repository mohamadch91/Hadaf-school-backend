from urllib import request
from uuid import uuid4
from django.db import models
import random
import string
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from courseDEP.models import *
from django.core.validators import RegexValidator
from datetime import timedelta
from django.utils import timezone

def send_otp(otp):
    print("otp password")
    print(otp.password)

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager
    """

    def create_user(self, phone, password, **extra_fields):
        # print("debug")
        print(phone)
        if not phone:
            raise ValueError('The phone must be set')

        # password=make_password(password)       
        # return self.create_user(username, password, **extra_fields)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password ,**extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    username = None
    phoneNumberRegex = RegexValidator(regex = r"^\+?98?\d{8,10}$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 13, unique = True)
    birth = models.DateField(blank=True,null=True)
    national_code=models.IntegerField(blank=True,null=True)
    role=models.CharField(max_length=10,blank=True,null=True)
    first_name =models.CharField(max_length=20,blank=True,null=True)
    last_name =models.CharField(max_length=20,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    picture=models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    USERNAME_FIELD='phone'
    objects = CustomUserManager()
    def __str__(self):
        return "{}".format(self.phone)

class Teacher(User):
    def __str__(self):
        return "{}".format(self.user.phone)

class Student(User):
    gpaverage=models.FloatField(blank=True,null=True)
    disipcline=models.FloatField(blank=True,null=True)
    school=models.CharField(max_length=20,blank=True,null=True)
    parentName=models.CharField(max_length=20,blank=True,null=True)
    parentNationalCode=models.IntegerField(blank=True,null=True)
    pbirthday=models.DateField(blank=True,null=True)
    peducation=models.CharField(max_length=20,blank=True,null=True)
    pjob=models.CharField(max_length=20,blank=True,null=True)
    address=models.CharField(max_length=20,blank=True,null=True)
    grade=models.ForeignKey(grade,on_delete=models.CASCADE,null=True)
    department=models.ForeignKey(department,on_delete=models.CASCADE,null=True)
    method='phone'
   
    def __str__(self):
        return "{}".format(self.user.phone)
class OtpRequestQuerySet(models.QuerySet):
    def is_valid(self, receiver, request, password):
        current_time = timezone.now()
        return self.filter(
            receiver=receiver,
            request_id=request,
            password=password,
            created__lt=current_time,
            created__gt=current_time-timedelta(seconds=120),

        ).exists()

class OTPManager(models.Manager):

    def get_queryset(self):
        return OtpRequestQuerySet(self.model, self._db)

    def is_valid(self, receiver, request, password):
        return self.get_queryset().is_valid(receiver, request, password)


    def generate(self, data):
        otp = self.model(receiver=data['receiver'])
        otp.save(using=self._db)
        send_otp(otp)
        return otp



def generate_otp():
    rand = random.SystemRandom()
    digits = rand.choices(string.digits, k=7 )
    return  ''.join(digits)


class OTPRequest(models.Model):

    request_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    receiver = models.IntegerField()
    password = models.CharField(max_length=7, default=generate_otp)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    objects = OTPManager()