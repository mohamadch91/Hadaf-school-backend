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
class quizHeaderView(APIView):

    def post(self, request):
        ser = quizHeaderSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser. errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveOfflineHeader = get_object_or_404(quizHeader, id=id)
        ser = quizHeaderSerializer(archiveOfflineHeader, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser. errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'c_id' in request.GET:
            id = request.GET['c_id']
            archiveOfflineHeader = quizHeader.objects.filter(course=id)
            ser = quizHeaderSerializer(archiveOfflineHeader,many=True) 
            new_data=copy.deepcopy(ser.data)
            new_data['course_name']=archiveOfflineHeader.course.name
            new_data['teacher_name']=archiveOfflineHeader.teacher.last_name
            return Response(new_data, status=status.HTTP_200_OK)
        else:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveOfflineHeader = get_object_or_404(quizHeader, id=id)
        archiveOfflineHeader.delete()
        return Response(status=status.HTTP_201_CREATED)


class quizQuestionView(APIView):

    def post(self, request):
        ans=[]
        for i in request.data:
            ser = quizQuestionSerializer(data=i)
            if ser.is_valid():
                ser.save()
                ans.append(ser.data)
        return Response(ans, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveFiles = get_object_or_404(quizQuestion, id=id)
        ser = quizQuestionSerializer(archiveFiles, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser. errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'h_id' in request.GET:
            id = request.GET['h_id']
            archiveFiles = quizQuestion.objects.filter(header_id=id)
            ser=quizQuestionSerializer(archiveFiles,many=True)
        else:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        return Response(ser.data)  

    def delete(self, request):
        for x in request.data:
            id=x["id"]
            archiveFiles= get_object_or_404(quizQuestion, id=id)
            archiveFiles.delete()
        return Response(status=status.HTTP_201_CREATED)


class studentQueezView(APIView):

    def post(self, request):
        ans=[]
        for i in request.data:    
            ser = studentQueezSerializer(data=i)
            if ser.is_valid():
                ser.save()
                ans.append(ser.data)
        return Response(ans, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveFiles = get_object_or_404(studentQueez, id=id)
        ser = studentQueezSerializer(archiveFiles, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser. errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'h_id' in request.GET and 's_id' not in request.GET:
            id = request.GET['h_id']
            archiveFiles = studentQueez.objects.filter(quizheader=id)
            ser= studentQueezSerializer(archiveFiles,many=True)
            new_data=copy.deepcopy(ser.data) 
            for i in new_data:
                header=get_object_or_404(quizHeader,id=i["quizheader"])
                i["header_name"]=header.description
                user=get_object_or_404(Student,pk=i["student"])
                i["student_name"]=user.phone
            return Response(new_data,status.HTTP_200_OK)    
        
        elif 'h_id' not in request.GET and 's_id'  in request.GET:
            id = request.GET['s_id']
            archiveFiles = studentQueez.objects.filter(student=id)
            ser= studentQueezSerializer(archiveFiles,many=True)
            new_data=copy.deepcopy(ser.data) 
            for i in new_data:
                header=get_object_or_404(quizHeader,id=i["quizheader"])
                i["header_name"]=header.description
                user=get_object_or_404(Student,pk=i["student"])
                i["student_name"]=user.phone
            return Response(new_data,status.HTTP_200_OK)
        elif 'h_id'  in request.GET and 's_id'  in request.GET:
            id = request.GET['s_id']
            h_id=request.GET['h_id']
            archiveFiles = studentQueez.objects.filter(student=id,quizheader=h_id)
            ser= studentQueezSerializer(archiveFiles,many=True)
            new_data=copy.deepcopy(ser.data) 
            for i in new_data:
                header=get_object_or_404(quizHeader,id=i["quizheader"])
                i["header_name"]=header.description
                user=get_object_or_404(Student,pk=i["student"])
                i["student_name"]=user.phone
            return Response(new_data,status.HTTP_200_OK)

        else:
            return Response('need query param',status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveFiles= get_object_or_404(studentQueez, id=id)
        archiveFiles.delete()
        return Response(status=status.HTTP_201_CREATED)
