from django.shortcuts import render

# Create your views here.

from queue import Empty
from turtle import clear
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


class ForumHeaderView(APIView):

    def post(self, request):
        ser = ForumHeaderSeriliazer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveOfflineHeader = get_object_or_404(ForumHeader, id=id)
        ser = ForumHeaderSeriliazer(archiveOfflineHeader, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'id' in request.GET:
            id = request.GET['id']
            archiveOfflineHeader = get_object_or_404(ForumHeader, id=id)
            ser = ForumHeaderSeriliazer(ForumHeader.objects.get(id=id))  
        else:
            ser = ForumHeaderSeriliazer(ForumHeader.objects.all(), many=True)
        return Response(ser.data)  

    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveOfflineHeader = get_object_or_404(ForumHeader, id=id)
        archiveOfflineHeader.delete()
        return Response(status=status.HTTP_201_CREATED)


class ForumDetailView(APIView):

    def post(self, request):
        ser = ForumDetailSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveFiles = get_object_or_404(ForumDetail, id=id)
        ser = ForumDetailSerializer(archiveFiles, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'id' in request.GET:
            id = request.GET['id']
            archiveFiles = get_object_or_404(ForumDetail, id=id)
            ser = ForumDetailSerializer(ForumDetail.objects.get(id=id))  
        else:
            ser = ForumDetailSerializer(ForumDetail.objects.all(), many=True)
        return Response(ser.data)  

    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        archiveFiles= get_object_or_404(ForumDetail, id=id)
        archiveFiles.delete()
        return Response(status=status.HTTP_201_CREATED)
