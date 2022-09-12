from cmath import exp
from itertools import count
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
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from django.shortcuts import get_object_or_404
from .models import *
from course.models import *
from authen.models import *
from package.models import *
from .serializers import *
from package.serializers import *
from discount.models import *
class dahsboardVIew(APIView):
    def get(self,request):
        studenr_count=Student.objects.all().count()
        courses=Course.objects.all().count()
        data={
            "s_count":studenr_count,
            "t_count":courses
        }
        return Response(data,status.HTTP_200_OK)

class admindahsboardVIew(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        studenr_count=Student.objects.all().count()
        courses=Course.objects.all().count()
        teacher_count=Teacher.objects.all().count()
        admin_count=User.objects.all().count()
        admin_count=admin_count-teacher_count-studenr_count
        data={
            "s_count":studenr_count,
            "courses":courses,
            "t_Count":teacher_count,
            "admin":admin_count
        }
        return Response(data,status.HTTP_200_OK)

class walletView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        id=request.user.id
        try:
            wallets=get_object_or_404(wallet,studentID=id)
        except:
            new_data={
                "amount":0,
                "studentID":id
            }
            serializer=walletSerializer(data=new_data)
            if serializer.is_valid():
                serializer.save()
                wallets=get_object_or_404(wallet,studentID=id)
        data={
            "amount":wallets.amount
        }
        return Response(data,status.HTTP_200_OK)     
    def post(self,request):
        s_wallet=get_object_or_404(wallet,studentID=request.data["studentID"])
        s_wallet.amount=s_wallet.amount+request.data["amount"]
        s_wallet.save()
        data={
            "amount":s_wallet.amount
        }
        return Response(data,status.HTTP_200_OK)

class basketView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        id=request.user.id
        baskets=basket.objects.filter(studentID=id)
        ans=[]
        for x in baskets:
            if x.type=='normal':
                normal=normalPackage.objects.get(id=x.buyID)
                course=normalPackageCourse.objects.filter(packageID=normal.id)
                #calculate price
                price=0
                for z in course:
                    if(z.courseID.price2!=None):
                        price=price+z.courseID.price2
                    else:
                        if z.courseID.price1 != None:
                            price=price+z.courseID.price1
                price=price*((100-normal.percent)/100) 
                ans.append({
                    "id":x.id,
                    "name":normal.name,
                    "percent":normal.percent,
                    "buy_id":normal.id,
                    "type":x.type,
                    "price":price
                })
            elif x.type=='timing':
                timing=timingPackage.objects.get(id=x.buyID)
                course=timingPackageCourse.objects.filter(packageID=normal.id)
                #calculate price
                price=0
                for z in course:
                    if(z.courseID.price2!=None):
                        price=price+z.courseID.price2
                    else:
                        if z.courseID.price1 != None:
                            price=price+z.courseID.price1
                price=price*((100-normal.percent)/100) 
                      
                ans.append({
                    "id":x.id,
                    "name":timing.name,
                    "percent":timing.percent,
                    "type":x.type,
                    "buy_id":timing.id,
                    "asDate":timing.asDate,
                    "toDate":timing.toDate,
                    "price":price
                })
            elif x.type=='student':
                student=studentPackage.objects.get(id=x.buyID)
                course=studentPackageCourse.objects.filter(packageID=normal.id)
                #calculate price
                price=0
                count_course=course.count()
                for z in course:
                    if(z.courseID.price2!=None):
                        price=price+z.courseID.price2
                    else:
                        if z.courseID.price1 != None:
                            price=price+z.courseID.price1
                m=studentPackageDiscount.objects.all()[0].percent
                price=price*((100-m*count_course)/100)


                ans.append({
                    "id":x.id,
                    "name":student.name,
                    "buy_id":student.id,
                    "type":x.type,
                    "price":price
                })
            elif x.type=='course':
                course=Course.objects.get(id=x.buyID)
                final_price=0
                if course.price1 != None:
                    final_price=course.price1
                if course.price2!=None:
                    final_price=course.price2
                
                ans.append({
                    "id":x.id,
                    "name":course.name,
                    "buy_id":course.id,
                    "type":x.type,
                    "price":final_price

                })
        final_price=0
        for k in ans:
            final_price+=k["price"]
        ans_data={
            "basket":ans,
            "final_price":final_price
        }
        return Response(ans_data,status.HTTP_200_OK)   
    def post(self,request):
        id=request.user.id
        ans=[]
        for i in request.data:
            new_data={
                "studentID":id,
                "type":i['type'],
                "buyID":i['buyID']
            }
            serializer=basketSerializer(data=new_data)
            if serializer.is_valid():
                serializer.save()
                ans.append(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(ans,status=status.HTTP_200_OK)
    def delete(self,request):
        for i in request.data:

            id=i['id']
            bas=get_object_or_404(basket,id=id)
            bas.delete()
        return Response(status=status.HTTP_200_OK)


class search(APIView):
    def get(self,request):
        id=request.user.id
        search=request.query_params.get('search','')
        ans=[]
        if search=='':
            return Response(ans,status=status.HTTP_200_OK)
        courses=Course.objects.filter(name__icontains=search,showforstudents=True,active=True)
        courses=Course.objects.filter(lessonID__name__icontains=search,showforstudents=True,active=True)|courses
        courses=Course.objects.filter(departmentID__name__icontains=search,showforstudents=True,active=True)|courses
        courses=Course.objects.filter(teacherID__last_name__icontains=search,showforstudents=True,active=True)|courses
        
        for x in courses:
            ans.append({
                "id":x.id,
                "name":x.name,
                "price":x.price1,
                "type":"course"
            })
        normal=normalPackage.objects.filter(name__icontains=search)
        price=0
        for x in normal:
            price=0
            np=normalPackageCourse.objects.filter(packageID=x.id)
            for y in np:
                if(y.courseID.showforstudents==True and y.courseID.active==True and y.courseID.price1 is not None):
                    price=price+y.courseID.price1
            ans.append({
                "id":x.id,
                "name":x.name,
                "price":price,
                "type":"normal"
            })
        timing=timingPackage.objects.filter(name__icontains=search)
        for x in timing:
            price=0
            np=timingPackageCourse.objects.filter(packageID=x.id)
            for y in np:
                if(y.courseID.showforstudents==True and y.courseID.active==True and y.courseID.price1 is not None):
                    price+=y.courseID.price1
            ans.append({
                "id":x.id,
                "name":x.name,
                "price":price,
                "type":"timing"
            })
      
        return Response(ans,status=status.HTTP_200_OK)

class discountView(APIView):
    def post(self,request):
        code=request.data["code"]
        discount=get_object_or_404(Discount,code=code)
        if discount.active==False:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if(discount.count>0):
            discount.count-=1
            discount.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        amount=request.data["amount"]
        if(discount.isPercent):
            amount=amount*((100-discount.amount)/100)
        else:
            amount=amount-discount.amount
        return Response({"amount":amount},status=status.HTTP_200_OK)
        
class discountUserview(APIView):
    def post(self,request):
        code=request.data["code"]
        discount=get_object_or_404(DiscountUser,code=code)
        amount=request.data["amount"]
        if(discount.percent is not None):
            amount=amount*((100-discount.percent)/100)
        else:
            amount=amount
        return Response({"amount":amount},status=status.HTTP_200_OK)

