# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json
from curses import A_PROTECT
from django.shortcuts import render

# Create your views here.
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
from rest_framework.permissions import IsAuthenticated

from dashboard.models import wallet,basket

# from authen.models import User
from .models import *
from package.models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from course.models import *
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
MERCHANT = '18cd0405-b44b-4c21-858b-c834f7a035f8'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
Amount = 10001  # Rial / Required
description = "backend test"  # Required
# Important: need to edit for realy server.
CallbackURL = 'https://api.srvschool.ir/zarinpal/verify/'
student_array = {}




def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        buys=get_object_or_404(buy,authority=t_authority)
        redirect=buy.url
        req_data = {
            "merchant_id": MERCHANT,
            "amount": buys.amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                wallets=get_object_or_404(wallet,studentID=buys.student.id)
                wallets.amount=wallets.amount+buys.amount
                wallets.save()
                return redirect(redirect)

                
            elif t_status == 101:
                return redirect(redirect)

            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')

class buyWalletView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        buy_mount=request.GET.get('amount')
        if buy_mount is None:
            return Response({'message':'amount is required'},status=status.HTTP_400_BAD_REQUEST)
        user=request.user
        user=get_object_or_404(Student,pk=user.id)
        buy_mount=int(buy_mount)
        wallets=get_object_or_404(wallet,studentID=user.id)
        baskets=basket.objects.filter(studentID=user.id)
        amount=wallets.amount
        if(amount <buy_mount):
            return Response({'message':'your amount is not enough'},status=status.HTTP_400_BAD_REQUEST)
        else:
            amount=amount-buy_mount
            wallets.amount=amount
            wallets.save()
            for basketi in baskets:
                for x in baskets:
                    if x.type=='normal':
                        normal=normalPackage.objects.get(id=x.buyID)
                        course=normalPackageCourse.objects.filter(packageID=normal.id)
                        #calculate price
                        for z in course:
                            course=get_object_or_404(Course,id=z.courseID)
                            s_c=StudetCourse.objects.create(studentID=user,courseID=course)
                            s_c.save()
                    elif x.type=='timing':
                        timing=timingPackage.objects.get(id=x.buyID)
                        course=timingPackageCourse.objects.filter(packageID=timing.id)
                        #calculate price
                        price=0
                        for z in course:
                            course=get_object_or_404(Course,id=z.courseID)
                            s_c=StudetCourse.objects.create(studentID=user,courseID=course)
                            s_c.save()
                            
                       
                    elif x.type=='student':
                        student=studentPackage.objects.get(id=x.buyID)
                        course=studentPackageCourse.objects.filter(packageID=student.id)
                        #calculate price
                        price=0
                        count_course=course.count()
                        for z in course:
                            course=get_object_or_404(Course,id=z.courseID)
                            s_c=StudetCourse.objects.create(studentID=user,courseID=course)
                            s_c.save()


                       
                    elif x.type=='course':
                        course=Course.objects.get(id=x.buyID)
                        s_c=StudetCourse.objects.create(studentID=user,courseID=course)
                        s_c.save()
                   
                    basketi.delete()
            return Response({'message':'your amount is enough'},status=status.HTTP_200_OK)





class addTowallet(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        amount=request.data["amount"]
        url=request.data["url"]
        user=request.user
        user=get_object_or_404(Student,pk=user.id)
        req_data = {
        "merchant_id": MERCHANT,
        "amount": Amount,
        "callback_url": CallbackURL,
        "description": description,
        
        }
        req_header = {"accept": "application/json",
                    "content-type": "application/json'"}
        req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
            req_data), headers=req_header)
        print(req.json())    
        if len(req.json()['errors']) == 0:
            authority = req.json()['data']['authority']
            #create new buy model
            buys=buy.objects.create(student=user,amount=Amount,authority=authority,url=url)
            buys.save()
            return Response(ZP_API_STARTPAY.format(authority=authority))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return Response(f"Error code: {e_code}, Error Message: {e_message}")
    