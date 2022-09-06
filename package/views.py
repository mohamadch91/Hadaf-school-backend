import re
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from queue import Empty
 
from urllib import request
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
from .models import *
from .serializers import *
import copy

class normalPackageView(APIView):
    def get(self, request):
        normalPackageList = normalPackage.objects.all()
        serializer = normalPackageSerializer(normalPackageList, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = normalPackageSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        id=request.data['id']
        normalPackageList = get_object_or_404(normalPackage, id=id)
        serializer = normalPackageSerializer(normalPackageList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        for i in request.data:
            id=i['id']
            normalPackageList = get_object_or_404(normalPackage, id=id)
            normalPackageList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class normalPackageCourseView(APIView):
    def get(self, request):
        p_id=request.query_params.get('p_id')
        normalPackageCourseList = normalPackageCourse.objects.filter(packageID=p_id)
        serializer = normalPackageCourseSerializer(normalPackageCourseList, many=True)
        new_data=copy.deepcopy(serializer.data)
        for i in new_data:
            course=get_object_or_404(Course, id=i['courseID'])
            package=get_object_or_404(normalPackage, id=i['packageID'])
            i['course_name']=course.name
            i['package_name']=package.name
        return Response(new_data)
    def post(self, request):
        ans=[]
        for i in request.data:
            serializer = normalPackageCourseSerializer(data=i)
            if serializer.is_valid():
                serializer.save()
                ans.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ans, status=status.HTTP_201_CREATED)
    def put(self, request):
        for  i in request.data:
            id=i["id"] 
            cpackage_cours=get_object_or_404(normalPackageCourse, id=id)
            serializer = normalPackageCourseSerializer(cpackage_cours, data=i)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)                    
    def delete(self, request):
        for i in request.data:
            id=i["id"] 
            cpackage_cours=get_object_or_404(normalPackageCourse, id=id)
            cpackage_cours.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class timingPackageView(APIView):
    def get(self, request):
        timingPackageList = timingPackage.objects.all()
        serializer = timingPackageSerializer(timingPackageList, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = timingPackageSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        for  i in request.data:
            id=i["id"] 
            cpackage_cours=get_object_or_404(timingPackage, id=id)
            serializer = timingPackageSerializer(cpackage_cours, data=i)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_202_ACCEPTED)
    def delete(self, request):
        for i in request.data:
            id=i["id"] 
            cpackage_cours=get_object_or_404(timingPackage, id=id)
            cpackage_cours.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       

class timingPackageCourseView(APIView):
    def get(self, request):
        p_id=request.query_params.get('p_id')
        timingPackageCourseList = timingPackageCourse.objects.filter(packageID=p_id)
        serializer = timingPackageCourseSerializer(timingPackageCourseList, many=True)
        new_data=copy.deepcopy(serializer.data)
        for i in new_data:
            course=get_object_or_404(Course, id=i['courseID'])
            package=get_object_or_404(timingPackage, id=i['packageID'])
            i['course_name']=course.name
            i['package_name']=package.name
        return Response(new_data)
    def post(self, request):
        ans=[]
        for i in request.data:
            serializer = timingPackageCourseSerializer(data=i)
            if serializer.is_valid():
                serializer.save()
                ans.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ans, status=status.HTTP_201_CREATED)
    def put(self, request):
        for  i in request.data:
            id=i["id"] 
            cpackage_cours=get_object_or_404(timingPackageCourse, id=id)
            serializer = timingPackageCourseSerializer(cpackage_cours, data=i)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)
    def delete(self, request):
        for i in request.data:
            id=i["id"] 
            cpackage_cours=get_object_or_404(timingPackageCourse, id=id)
            cpackage_cours.delete()
        return Response(status=status.HTTP_201_CREATED)


class studentPackageView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        s_id=request.query_params.get('s_id')
        studentPackageList = studentPackage.objects.filter(student=s_id)
        ans=[]
        for i in studentPackageList:
            ser=studentPackageSerializer(i)
            new_data=copy.deepcopy(ser.data)
            student=get_object_or_404(Student, id=new_data['student'])
            new_data['student_name']=student.first_name+student.last_name
            ans.append(new_data)
        return Response(ans)
    def post(self, request):
        serializer = studentPackageSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        for  i in request.data:
            id=i["id"] 
            cpackage_cours=get_object_or_404(studentPackage, id=id)
            serializer = studentPackageSerializer(cpackage_cours, data=i)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)
    def delete(self, request):
        for i in request.data:
            id=i["id"] 
            cpackage_cours=get_object_or_404(studentPackage, id=id)
            cpackage_cours.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class studentPackageCourseView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        p_id=request.query_params.get('p_id')
        studentPackageCourseList = studentPackageCourse.objects.filter(packageID=p_id)
        serializer = studentPackageCourseSerializer(studentPackageCourseList, many=True)
        new_data=copy.deepcopy(serializer.data)
        for i in new_data:
            course=get_object_or_404(Course, id=i['courseID'])
            package=get_object_or_404(studentPackage, id=i['packageID'])
            i['course_name']=course.name
            i['package_name']=package.name
        return Response(new_data)
    def post(self, request):
        ans=[]
        for i in request.data:
            serializer = studentPackageCourseSerializer(data=i)
            if serializer.is_valid():
                serializer.save()
                ans.append(serializer.data)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ans, status=status.HTTP_201_CREATED)
    def put(self, request):
        for  i in request.data:
            id=i["id"] 
            cpackage_cours=get_object_or_404(studentPackageCourse, id=id)
            serializer = studentPackageCourseSerializer(cpackage_cours, data=i)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)
    def delete(self, request):
        for i in request.data:
            id=i["id"] 
            cpackage_cours=get_object_or_404(studentPackageCourse, id=id)
            cpackage_cours.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class studentPackageDiscountView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        studentPackageDiscountList = studentPackageDiscount.objects.all()
        serializer = studentPackageDiscountSerializer(studentPackageDiscountList, many=True)
        return Response(serializer.data)
    def post(self, request):
        studentPackageDiscount.objects.all().delete()
        serializer = studentPackageDiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        id=request.data["id"]
        studentPackageDiscountList = get_object_or_404(studentPackageDiscount, id=id)
        serializer = studentPackageDiscountSerializer(studentPackageDiscountList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        id=request.data["id"]
        studentPackageDiscountList = get_object_or_404(studentPackageDiscount, id=id)
        studentPackageDiscountList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)