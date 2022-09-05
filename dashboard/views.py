from itertools import count
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
from package.models import *
from .serializers import *
from package.serializers import *

class dahsboardVIew(APIView):
    def get(self,request):
        studenr_count=Student.objects.all().count()
        courses=Course.objects.all().count()
        data={
            "s_count":studenr_count,
            "t_count":courses
        }
        return Response(data,status.HTTP_200_OK)

class admindahsboardVIew(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        studenr_count=Student.objects.all().count()
        courses=Course.objects.all().count()
        teacher_count=Teacher.objects.all().count()
        admin_count=User.objects.all().count()
        admin_count=admin_count-teacher_count-studenr_count
        data={
            "s_count":studenr_count,
            "courses":courses,
            "t_Count":teacher_count,
            "admin":admin_count
        }
        return Response(data,status.HTTP_200_OK)

class walletView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        id=request.user.id
        wallets=wallet.objects.get(studentID=id)
        data={
            "amount":wallets.amount
        }
        return Response(data,status.HTTP_200_OK)     

class basketView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        id=request.user.id
        baskets=basket.objects.filter(studentID=id)
        ans=[]
        for x in baskets:
            if x.type=='normal':
                normal=normalPackage.objects.get(id=x.buyID)
                ans.append({
                    "id":x.id,
                    "name":normal.name,
                    "percent":normal.percent,
                    "type":x.type
                })
            elif x.type=='timing':
                timing=timingPackage.objects.get(id=x.buyID)
                ans.append({
                    "id":x.id,
                    "name":timing.name,
                    "percent":timing.percent,
                    "type":x.type,
                    "asDate":timing.asDate,
                    "toDate":timing.toDate
                })
            elif x.type=='student':
                student=studentPackage.objects.get(id=x.buyID)
                ans.append({
                    "id":x.id,
                    "name":student.name,
                    "type":x.type
                })
            elif x.type=='course':
                course=Course.objects.get(id=x.buyID)
                ans.append({
                    "id":x.id,
                    "name":course.name,
                    "type":x.type
                })
        return Response(ans,status.HTTP_200_OK)   
    def post(self,request):
        id=request.user.id
        type=request.data['type']
        buyID=request.data['buyID']
        basket.objects.create(studentID_id=id,type=type,buyID=buyID)
        return Response(status=status.HTTP_200_OK)
    def delete(self,request):
        id=request.data['id']
        basket.objects.get(id=id).delete()
        return Response(status=status.HTTP_200_OK)