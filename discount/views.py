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


class DiscountView(APIView):

    def post(self, request):
        ser = discountSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        discount = get_object_or_404(Discount, id=id)
        ser = discountSerializer(discount, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'id' in request.GET:
            id = request.GET['id']
            discount = get_object_or_404(Discount, id=id)
            ser = discountSerializer(Discount.objects.get(id=id))  
        else:
            ser = discountSerializer(Discount.objects.all(), many=True)
        return Response(ser.data)  

    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        discount= get_object_or_404(Discount, id=id)
        Discount.delete()
        return Response(status=status.HTTP_201_CREATED)



class DiscountCourseView(APIView):
    def post(self, request):
        ser = discountCourseSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        discountCourse = get_object_or_404(DiscountCourse, id=id)
        ser = discountCourseSerializer(discountCourse, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'id' in request.GET:
            id = request.GET['id']
            discount = get_object_or_404(DiscountCourse, id=id)
            ser = discountCourseSerializer(DiscountCourse.objects.get(id=id))  
        else:
            ser = discountCourseSerializer(DiscountCourse.objects.all(), many=True)
        return Response(ser.data)  

    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        discountCourse= get_object_or_404(DiscountCourse, id=id)
        DiscountCourse.delete()
        return Response(status=status.HTTP_201_CREATED)


