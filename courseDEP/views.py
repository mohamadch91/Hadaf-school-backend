from ast import Delete
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from .serializers import *
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
# Create your views here.

class gradeView(APIView):

    def post (self,request):
        ser=gradeSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        ser=gradeSerializer(grade.objects.all(),many=True)
        return Response(ser.data)

    def put(self,request):
        if( 'id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            grade=get_object_or_404(grade,id=id)
            ser=gradeSerializer(grade,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        if('id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            grades=get_object_or_404(grade,id=id)
            grades.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
class departmentView(APIView):
    def post (self,request):
        ser=departmentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        ser=departmentSerializer(department.objects.all(),many=True)
        return Response(ser.data)
    def put(self,request):
        if( 'id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            Department=get_object_or_404(department,id=id)
            ser=departmentSerializer(Department,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        if('id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            Department=get_object_or_404(department,id=id)
            Department.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class lessonsView(APIView):


    def get(self,request):
        ser=lessonSerializer(lessons.objects.all(),many=True)
        return Response(ser.data)
    def post(self,request):
        ser=lessonSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        if( 'id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            lesson=get_object_or_404(lessons,id=id)
            ser=lessonSerializer(lesson,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        if('id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            lesson=get_object_or_404(lessons,id=id)
            lesson.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
class daysView(APIView):

    def get(self,request):
        ser=daysSerializer(days.objects.all(),many=True)
        return Response(ser.data)
    def post(self,request):
        ser=daysSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        if( 'id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            day=get_object_or_404(days,id=id)
            ser=daysSerializer(day,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        if('id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            day=get_object_or_404(days,id=id)
            day.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
class yearView(APIView):
    
    def get(self,request):
        ser=yearSerializer(year.objects.all(),many=True)
        return Response(ser.data)
    def post(self,request):
        ser=yearSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        if( 'id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            years=get_object_or_404(year,id=id)
            ser=yearSerializer(years,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        if('id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            years=get_object_or_404(year,id=id)
            years.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class CourseTypeView(APIView):
        
    def get(self,request):
        ser=CourseTypeSerializer(CourseType.objects.all(),many=True)
        return Response(ser.data)
    def post(self,request):
        ser=CourseTypeSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        if( 'id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            CourseTypes=get_object_or_404(CourseType,id=id)
            ser=CourseTypeSerializer(CourseTypes,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        if('id' not in request.data):
            return Response("id is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            id=request.data['id']
            CourseTypes=get_object_or_404(CourseType,id=id)
            CourseTypes.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
