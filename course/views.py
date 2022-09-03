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

class courseView(APIView):

    def post(self, request):
        ser = courseSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        course = get_object_or_404(Course, id=id)
        ser = courseSerializer(course, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if 'id' in request.GET :
            id = request.GET['id']
            course = get_object_or_404(Course, id=id)
            ser = courseSerializer(Course.objects.get(id=id))
        else:
            ser = courseSerializer(Course.objects.all(), many=True)
        return Response(ser.data)  
    
    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        course = get_object_or_404(Course, id=id)
        course.delete()
        return Response(status=status.HTTP_201_CREATED)


class studentCourseView(APIView):

    def post(self, request):
        ans=[]
        for item in request.data:
            block=BlocedStudent.objects.filter(student=item['studentID'],course=item['courseID'])
            if(block.count()==0):
                return Response('student is blocked', status=status.HTTP_400_BAD_REQUEST)
            ser = studentCourseSerializer(data=item)
            if ser.is_valid():
                ser.save()
                ans.append(ser.data)
            else:
                return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(ans,status=status.HTTP_201_CREATED)
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data["id"]
        studentCourse = get_object_or_404(StudetCourse, id=id)
        ser = studentCourseSerializer(studentCourse, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if 'id' in request.GET :
            id = request.GET['id']
            studentCourse = get_object_or_404(StudetCourse, id=id)
            ser = studentCourseSerializer(StudetCourse.objects.get(id=id))
        else:
            ser = studentCourseSerializer(StudetCourse.objects.all(), many=True)
        return Response(ser.data)  

    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        studentCourse = get_object_or_404(StudetCourse, id=id)
        studentCourse.delete()
        return Response(status=status.HTTP_201_CREATED)

class CourseHomeWorkView(APIView):

    def post(self, request):
        ser = courseHomeWorkSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        courseHomeWork = get_object_or_404(CourseHomeWork, id=id)
        ser = courseHomeWorkSerializer(courseHomeWork, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'id' in request.GET:
            id = request.GET['id']
            courseHomeWork = get_object_or_404(CourseHomeWork, id=id)
            ser = courseHomeWorkSerializer(CourseHomeWork.objects.get(id=id))  
        else:
            ser = courseHomeWorkSerializer(CourseHomeWork.objects.all(), many=True)
        return Response(ser.data)  

    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        courseHomeWork = get_object_or_404(CourseHomeWork, id=id)
        courseHomeWork.delete()
        return Response(status=status.HTTP_201_CREATED)


class CourseDaysView(APIView):

    def post(self, request):
        ser = courseDaysSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        courseDays = get_object_or_404(CourseDays, id=id)
        ser = courseTypeSerializer(courseDays, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'id' in request.GET:
            id = request.GET['id']
            courseDays = get_object_or_404(CourseDays, id=id)
            ser = courseDaysSerializer(CourseDays.objects.get(id=id))  
        else:
            ser = courseDaysSerializer(CourseDays.objects.all(), many=True)
        return Response(ser.data)  

    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        courseDays = get_object_or_404(CourseDays, id=id)
        CourseDays.delete()
        return Response(status=status.HTTP_201_CREATED)



class CourseTypeView(APIView):

    def post(self, request):
        ser = courseTypeSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        courseType = get_object_or_404(CourseType, id=id)
        ser = courseTypeSerializer(courseType, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.error(), status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        if 'id' in request.GET:
            id = request.GET['id']
            courseType = get_object_or_404(CourseType, id=id)
            ser = courseTypeSerializer(CourseType.objects.get(id=id))  
        else:
            ser = courseTypeSerializer(CourseType.objects.all(), many=True)
        return Response(ser.data)  

    def delete(self, request):
        if 'id' not in request.data:
            return Response('id is required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        courseType = get_object_or_404(CourseType, id=id)
        CourseType.delete()
        return Response(status=status.HTTP_201_CREATED)




class teacherCourse(APIView):
    def get(self,request):
        id=request.query_params.get('id',None)
        if(id is  None):
            return Response("need query params",status=status.HTTP_400_BAD_REQUEST)
        courses=Course.objects.filter(teacherID=id)
        ser=courseSerializer(courses,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)

class coursegetHomeVIew(APIView):
    def get(self,request):
        id=request.query_params.get('id',None)
        if(id is  None):
            return Response("need query params",status=status.HTTP_400_BAD_REQUEST)
        hw=CourseHomeWork.objects.filter(courseID=id)
        hw_Ser=courseHomeWorkSerializer(hw,many=True)
        return Response(hw_Ser.data,status=status.HTTP_200_OK)
        
class specifiecStudentcourse(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        id=request.query_params.get('id',None)
        if(id  is None):
            return Response("need query params",status=status.HTTP_400_BAD_REQUEST)
        student=get_object_or_404(Student,pk=id)
        courses=StudetCourse.objects.filter(studentID=student.pk)
        ser=studentCourseSerializer(courses,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
        
# class addstudentCourse(APIView):
#     permission_classes=(IsAuthenticated,)
#     def get()