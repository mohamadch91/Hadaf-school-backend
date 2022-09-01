from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from re import I
from django.shortcuts import render

# Create your views here.
import json
from os import stat
from urllib import response
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated

# from authen.models import User
from .models import *

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .smsHelper import sms_list
class smsList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        x=sms_list()
        print(x)
        return Response(x)
