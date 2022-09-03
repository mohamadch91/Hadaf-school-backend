
from copy import copy
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
class ArchiveOfflineHeaderView(APIView):

    def post(self, request):
        ser = archiveOfflineHeaderSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveOfflineHeader = get_object_or_404(ArchiveOfflineHeader, id=id)
        ser = archiveOfflineHeaderSerializer(archiveOfflineHeader, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'c_id' in request.GET:
            id = request.GET['c_id']
            archiveOfflineHeader = ArchiveOfflineHeader.objects.filter(courseID=id)
            ser = archiveOfflineHeaderSerializer(archiveOfflineHeader,many=True)  
            copy_Ser=copy.deepcopy(ser.data)
            for i in copy_Ser:
                courses=get_object_or_404(Course,id=i['courseID'])
                i['courseName']=courses.name
        else:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        return Response(copy_Ser)  

    def delete(self, request):
        for x in request.data:
            archiveFiles= get_object_or_404(ArchiveFiles, id=x['id'])
            archiveFiles.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class ArchiveFilesView(APIView):

    def post(self, request):
        ser = archiveFilesSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveFiles = get_object_or_404(ArchiveFiles, id=id)
        ser = archiveFilesSerializer(archiveFiles, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'a_id' in request.GET:
            id = request.GET['a_id']
            archiveFiles = ArchiveFiles.objects.filter(archiveHeaderID=id)
            ser = archiveFilesSerializer(archiveFiles,many=True)
            copy_Ser=copy.deepcopy(ser.data)
            for i in copy_Ser:
                archiveOfflineHeader=get_object_or_404(ArchiveOfflineHeader,id=i['archiveHeaderID'])
                i['archiveHeaderTitle']=archiveOfflineHeader.title

        else:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        return Response(copy_Ser)  

    def delete(self, request):
        for x in request.data:
            archiveFiles= get_object_or_404(ArchiveFiles, id=x['id'])
            archiveFiles.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
