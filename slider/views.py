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
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# from authen.models import User
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class SliderView(APIView):
    def get(self,request):
        slider=Slider.objects.all()
        serializer=SliderSerializer(slider,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        id=request.data['id']
        slider=get_object_or_404(Slider,id=id)
        serializer=SliderSerializer(slider,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        id=request.data['id']
        slider=get_object_or_404(Slider,id=id)
        slider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BannerView(APIView):
    def get(self,reuqest):
        banner=Banner.objects.all()
        serializer=BannerSerializer(banner,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=BannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        id=request.data['id']
        banner=get_object_or_404(Banner,id=id)
        serializer=BannerSerializer(banner,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        id=request.data['id']
        banner=get_object_or_404(Banner,id=id)
        banner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    