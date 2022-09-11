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
            ans=[]
            for z in archiveOfflineHeader:
                ser=quizHeaderSerializer(z)
                i=copy.deepcopy(ser.data)
                i['course_name']=z.course.name
                i['teacher_name']=z.teacher.last_name
                ans.append(i)
            return Response(ans, status=status.HTTP_200_OK)
        elif 'id' in request.GET:
            id = request.GET['id']
            archiveOfflineHeader = get_object_or_404(quizHeader, id=id)
            ser=quizHeaderSerializer(archiveOfflineHeader)
            i=copy.deepcopy(ser.data)
            i['course_name']=archiveOfflineHeader.course.name
            i['teacher_name']=archiveOfflineHeader.teacher.last_name
            return Response(i, status=status.HTTP_200_OK)
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
        return Response(ans, status=status.HTTP_200_OK)
    
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
            else:
                return Response(ser. errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ans, status=status.HTTP_200_OK)
    
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

class studentResult(APIView):
    def get(self,request):
        s_id=request.query_params.get('s_id',None)
        h_id=request.query_params.get('h_id',None)
        if s_id is not None and h_id is not None:
            student=get_object_or_404(Student,pk=s_id)
            quizHeaders=get_object_or_404(quizHeader,id=h_id)
            studentQueezs=studentQueez.objects.filter(student=student,quizheader=quizHeaders)
            q_count=quizHeaders.question_count
            correct_count=0
            for i in studentQueezs:
                if i.result==i.question.result:
                    correct_count+=1
            return Response({'correct_count':correct_count,'q_count':q_count},status.HTTP_200_OK)
        else:
            return Response('need query param',status.HTTP_400_BAD_REQUEST)

class totalquizHeaderView(APIView):
    def get(self,request):
        id=request.query_params.get('id',None)
        if(id is not None ):
            totals=get_object_or_404(totalquizHeader,id=id)
            ser=totalquizHeaderSerializer(totals,many=False)
            return Response(ser.data,status.HTTP_200_OK)
        totals=totalquizHeader.objects.all()
        ser=totalquizHeaderSerializer(totals,many=True)
        return Response(ser.data,status.HTTP_200_OK)
    def post(self,request):
        ser=totalquizHeaderSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status.HTTP_201_CREATED)
        return Response(ser.errors,status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        id=request.data['id']
        total=get_object_or_404(totalquizHeader,id=id)
        ser=totalquizHeaderSerializer(total,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status.HTTP_201_CREATED)
        return Response(ser.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        id=request.data['id']
        total=get_object_or_404(totalquizHeader,id=id)
        total.delete()
        return Response(status.HTTP_201_CREATED)


class totalquizSubjectsView(APIView):
    def get(self,request):
        h_id=request.query_params.get('h_id',None)
        if h_id is not None:
            total=get_object_or_404(totalquizHeader,id=h_id)
            subjects=totalquizSubjects.objects.filter(quizheader=total)
            ser=totalquizSubjectsSerializer(subjects,many=True)
            return Response(ser.data,status.HTTP_200_OK)
        else:
            return Response('need query param',status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        ser=totalquizSubjectsSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status.HTTP_201_CREATED)
        return Response(ser.errors,status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        id=request.data['id']
        total=get_object_or_404(totalquizSubjects,id=id)
        ser=totalquizSubjectsSerializer(total,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status.HTTP_201_CREATED)
        return Response(ser.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        id=request.data['id']
        total=get_object_or_404(totalquizSubjects,id=id)
        total.delete()
        return Response(status.HTTP_201_CREATED)

class totalquizQuestionsView(APIView):
        def get(self,request):
            h_id=request.query_params.get('h_id',None)
            s_id=request.query_params.get('s_id',None)
            if h_id is not None and s_id is not None:
                total=get_object_or_404(totalquizHeader,id=h_id)
                subject=get_object_or_404(totalquizSubjects,id=s_id)
                questions=totalquizQuestion.objects.filter(header_id=total,subject=subject)
                ser=totalquizQuestionSerializer(questions,many=True)
                return Response(ser.data,status.HTTP_200_OK)
            elif h_id is not None:
                total=get_object_or_404(totalquizHeader,id=h_id)
                questions=totalquizQuestion.objects.filter(header_id=total)
                ser=totalquizQuestionSerializer(questions,many=True)
                return Response(ser.data,status.HTTP_200_OK)
            else:
                return Response('need query param',status.HTTP_400_BAD_REQUEST)
        def post(self,request):
            for i in request.data:
                ser=totalquizQuestionSerializer(data=i)
                if ser.is_valid():
                    ser.save()
                else:
                    return Response(ser.errors,status.HTTP_400_BAD_REQUEST)
            return Response(status.HTTP_201_CREATED)
        def put(self,request):
            id=request.data['id']
            total=get_object_or_404(totalquizQuestion,id=id)
            ser=totalquizQuestionSerializer(total,data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data,status.HTTP_201_CREATED)
            return Response(ser.errors,status.HTTP_400_BAD_REQUEST)
        def delete(self,request):
            id=request.data['id']
            total=get_object_or_404(totalquizQuestion,id=id)
            total.delete()
            return Response(status.HTTP_204_NO_CONTENT)

class totalstudentQueezView(APIView):
    def get(self,request):
        s_id=request.query_params.get('s_id',None)
        h_id=request.query_params.get('h_id',None)
        if s_id is not None and h_id is not None:
            student=get_object_or_404(Student,pk=s_id)
            quizHeaders=get_object_or_404(totalquizHeader,id=h_id)
            studentQueezs=totalstudentQueez.objects.filter(student=student,quizheader=quizHeaders)
            ser=totalstudentQueezSerializer(studentQueezs,many=True)
            return Response(ser.data,status.HTTP_200_OK)
        else:
            return Response('need query param',status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        for i in request.data:
            ser=totalstudentQueezSerializer(data=i)
            if ser.is_valid():
                ser.save()
            else:
                return Response(ser.errors,status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_201_CREATED)
    def put(self,request):
        id=request.data['id']
        total=get_object_or_404(totalstudentQueez,id=id)
        ser=totalstudentQueezSerializer(total,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status.HTTP_201_CREATED)
        return Response(ser.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        id=request.data['id']
        total=get_object_or_404(totalstudentQueez,id=id)
        total.delete()
        return Response(status.HTTP_201_CREATED)