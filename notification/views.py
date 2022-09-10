from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

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
from .serializers import *
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from django.shortcuts import get_object_or_404
from .models import *
import copy
from django.contrib.auth.hashers import make_password

class notificationView(APIView):
    def get(self, request):
        notifications = notification.objects.all()
        serializer = notificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = notificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        id=request.data['id']
        notifications = get_object_or_404(notification, id=id)
        serializer = notificationSerializer(notifications, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        id=request.data['id']
        notifications = get_object_or_404(notification, id=id)
        notifications.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class studentNotificationView(APIView):
    def get(self, request):
        s_id=request.query_params.get('s_id',None)
        if s_id:
            studentNotifications = studentNotification.objects.filter(student=s_id)
            ans=[]
            for x in studentNotifications:
                data={
                    'id':x.id,
                    'title':x.notification.title,
                    'description':x.notification.description,
                    'student':x.student.pk,
                }
                ans.append(data)
            return Response(ans)
        else:
            studentNotifications = studentNotification.objects.all()
            ans=[]
            for x in studentNotifications:
                data={
                    'id':x.id,
                    'title':x.notification.title,
                    'description':x.notification.description,
                    'student':x.student.pk,
                }
                ans.append(data)
            return Response(ans)

    def post(self, request):
        for i in request.data['students']:
            ser=studentNotificationSerializer(data={'student':i,'notification':request.data['notification']})
            if ser.is_valid():
                ser.save()
            else:
                return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)
    
    def put(self, request):
        id=request.data['id']
        studentNotifications = get_object_or_404(studentNotification, id=id)
        serializer = studentNotificationSerializer(studentNotifications, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        s_id=request.data['s_id']
        s_not=studentNotification.objects.filter(student=s_id)
        for i in s_not:
            data={
                "notification":i.notification.id,
                "student":i.student.pk
            }
            serializer = studentNotificationReadSerializer( data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            i.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class readedView(APIView):
    def get(self,request):
        s_id=request.query_params.get('s_id',None)
        n_id=request.query_params.get('n_id',None)
        if s_id and n_id:
            ans=[]
            s_not=studentNotificationRead.objects.filter(student=s_id,notification=n_id)
            for x in s_not:
                data={
                    'id':x.id,
                    'title':x.notification.title,
                    'description':x.notification.description,
                    'student':x.student.pk,
                    'readed':x.created_at
                }
                ans.append(data)
            return Response(ans)
        elif s_id:
            ans=[]
            s_not=studentNotificationRead.objects.filter(student=s_id)
            for x in s_not:
                data={
                    'id':x.id,
                    'title':x.notification.title,
                    'description':x.notification.description,
                    'student':x.student.pk,
                    'readed':x.created_at
                }
                ans.append(data)
            return Response(ans)
        elif n_id:
            ans=[]
            s_not=studentNotificationRead.objects.filter(notification=n_id)
            for x in s_not:
                data={
                    'id':x.id,
                    'title':x.notification.title,
                    'description':x.notification.description,
                    'student':x.student.pk,
                    'readed':x.created_at
                }
                ans.append(data)
            return Response(ans)
        else:
            s_not=studentNotificationRead.objects.all()
            ans=[]
            for x in s_not:
                data={
                    'id':x.id,
                    'title':x.notification.title,
                    'description':x.notification.description,
                    'student':x.student.pk,
                    'readed':x.created_at
                }
                ans.append(data)
            return Response(ans)