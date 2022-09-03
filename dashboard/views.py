from django.shortcuts import render

# Create your views here.
from queue import Empty
 
from urllib import request
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from authen.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from django.shortcuts import get_object_or_404
from .models import *
from course.models import *
from authen.models import *


class dahsboardVIew(APIView):
    def get(self,request):
        studenr_count=Student.objects.all().count()
        courses=Course.objects.all().count()
        data={
            "s_count":studenr_count,
            "t_count":courses
        }
        return Response(data,status.HTTP_200_OK)