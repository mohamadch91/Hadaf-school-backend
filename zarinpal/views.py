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
from authen.serializers import *
# Create your views here.
import json
from os import stat
from urllib import response
from django.shortcuts import render
import copy
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
        redirects=buys.url
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
                wallets.amount=wallets.amount+(buys.amount/10)
                wallets.save()
                return redirect(redirects)

                
            elif t_status == 101:
                return redirect(redirects)

            else:
                return redirect(redirects)
        else:
            return redirect(redirects)
    else:
        return redirect(redirects)
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
           
            for basketi in baskets:
                for x in baskets:
                    if x.type=='normal':
                        normal=normalPackage.objects.get(id=x.buyID)
                        course=normalPackageCourse.objects.filter(packageID=normal.id)
                        #calculate price
                        for z in course:
                            course=get_object_or_404(Course,id=z.courseID)
                            try:
                                test=get_object_or_404(StudetCourse,studentID=user.id,courseID=course.id)
                                return Response({'message':'you have this course'},status=status.HTTP_400_BAD_REQUEST)

                            except:
                                s_c=StudetCourse.objects.create(studentID=user,courseID=course)
                                s_c.save()
                    elif x.type=='timing':
                        timing=timingPackage.objects.get(id=x.buyID)
                        course=timingPackageCourse.objects.filter(packageID=timing.id)
                        #calculate price
                        price=0
                        for z in course:
                            course=get_object_or_404(Course,id=z.courseID)
                            try:
                                test=get_object_or_404(StudetCourse,studentID=user.id,courseID=course.id)
                                return Response({'message':'you have this course'},status=status.HTTP_400_BAD_REQUEST)

                            except:
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
                            try:
                                test=get_object_or_404(StudetCourse,studentID=user.id,courseID=course.id)
                                return Response({'message':'you have this course'},status=status.HTTP_400_BAD_REQUEST)

                            except:
                                s_c=StudetCourse.objects.create(studentID=user,courseID=course)
                                s_c.save()

                       
                    elif x.type=='course':
                        course=Course.objects.get(id=x.buyID)
                        try:
                            test=get_object_or_404(StudetCourse,studentID=user.id,courseID=course.id)
                            return Response({'message':'you have this course'},status=status.HTTP_400_BAD_REQUEST)
                        except:
                            s_c=StudetCourse.objects.create(studentID=user,courseID=course)
                            s_c.save()
                    basketi.delete()
            amount=amount-buy_mount
            wallets.amount=amount
            wallets.save()        
            
            return Response({'message':'your amount is enough'},status=status.HTTP_200_OK)





class addTowallet(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        amount=request.data["amount"]
        amount=int(amount)*10
        url=request.data["url"]
        user=request.user
        user=get_object_or_404(Student,pk=user.id)
        req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
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
            buys=buy.objects.create(student=user,amount=amount,authority=authority,url=url)
            buys.save()
            return Response(ZP_API_STARTPAY.format(authority=authority))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return Response(f"Error code: {e_code}, Error Message: {e_message}")

class report(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        s_id=request.query_params.get('s_id',None)
        price_from=request.query_params.get('price_from',None)
        price_to=request.query_params.get('price_to',None)
        # date_from=request.query_params.get('date_from',None)
        # date_to=request.query_params.get('date_to',None)
        buys_basket=buy.objects.all()
        # if s_id is not None:
        #     student=get_object_or_404(Student,phone=s_id)
        #     buys_basket=buy.objects.filter(student=student.pk)
        # if price_from is not None:
        #     buys_basket=buy.objects.filter(amount__gte=price_from)
        # if price_to is not None:
        #     buys_basket=buy.objects.filter(amount__lte=price_to)
        # # if date_from is not None:
        # #     buys_basket=buy.objects.filter(created_at__gte=date_from)
        # # if date_to is not None:
        # #     buys_basket=buy.objects.filter(updated_at__lte=date_to)
        serializer=buySerializer(buys_basket,many=True)
        new_data=copy.deepcopy(serializer.data)
        for i in new_data:
            student=get_object_or_404(Student,id=i['student'])
            ser=StudentSerializer(student)
            i['student_phone']=ser.data["phone"]
            i['student_name']=ser.data["first_name"]+" "+ser.data["last_name"]
            i["student_national_code"]=ser.data["national_code"]
        return Response(new_data,status=status.HTTP_200_OK)
        

        
