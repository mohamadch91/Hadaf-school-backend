from django.shortcuts import render

# Create your views here.

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
import copy
from django.contrib.auth.hashers import make_password
from .live_helper import *

class liveView(APIView):
    def post(self,request):
        ans=create(request.data["name"],request.data["id"])
        return Response(ans,status.HTTP_200_OK)

class joinView(APIView):
    def post(self,request):
        ans=join(request.data["name"],request.data["id"])
        return Response(ans,status.HTTP_200_OK)

class student_joinView(APIView):
    def post(self,request):
        ans=student_join(request.data["name"],request.data["id"])
        return Response(ans,status.HTTP_200_OK)

class getMeetings(APIView):
    def get(self,request):
        ans=getmeetings()
        return Response(ans,status.HTTP_200_OK)