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

class ForumHeaderView(APIView):
    permission_classes=(IsAuthenticated)
    def post(self, request):
        user=request.user
        new_data=copy.deepcopy(request.data)
        new_data["Userid"]=user.pk
        ser = ForumHeaderSeriliazer(data=new_data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveOfflineHeader = get_object_or_404(ForumHeader, id=id)
        ser = ForumHeaderSeriliazer(archiveOfflineHeader, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'c_id' in request.GET:
            id = request.GET['c_id']
            forumH=ForumHeader.objects.filter(course_id=id)
            ser = ForumHeaderSeriliazer(forumH, many=True)
            new_data=copy.deepcopy(ser.data)
            for x in new_data:
                user=User.objects.get(id=x["Userid"])
                x["Username"]=user.last_name+" "+user.first_name
                x["course_name"]=Course.objects.get(id=x["course_id"]).name

        else:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        return Response(ser.data)  

    def delete(self, request):
        for x in request.data:
           archiveFiles= get_object_or_404(ForumHeader, id=x["id"])
           archiveFiles.delete()
        return Response(status=status.HTTP_201_CREATED)


class ForumDetailView(APIView):

    def post(self, request):
        new_data=copy.deepcopy(request.data)
        new_data["Userid"]=request.user.pk
        ser = ForumDetailSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveFiles = get_object_or_404(ForumDetail, id=id)
        ser = ForumDetailSerializer(archiveFiles, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'h_id' in request.GET:
            id = request.GET['h_id']
            archiveFiles = ForumDetail.objects.filter(ForumHeaderid=id)
            ser = ForumDetailSerializer(archiveFiles, many=True) 
            new_data=copy.deepcopy(ser.data)
            for x in new_data:
                user=User.objects.get(id=x["Userid"])
                x["Username"]=user.last_name+" "+user.first_name

        else:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        return Response(ser.data)  

    def delete(self, request):
        for x in request.data:
              archiveFiles= get_object_or_404(ForumDetail, id=x["id"])
              archiveFiles.delete()
        return Response(status=status.HTTP_201_CREATED)
