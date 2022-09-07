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
import copy
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
            i =copy.deepcopy(ser.data)
            teacher=""
            department=""
            grade=""
            course_tye=""
            lesson=""
            year=""
            user=""
            if course.teacherID:
                if(course.teacherID.last_name and course.teacherID.first_name):
                    teacher=course.teacherID.last_name+" "+course.teacherID.first_name
                else:
                    teacher=course.teacherID.phone
            if  course.departmentID:
                department=course.departmentID.name
            if(course.gradeID):
                grade=course.gradeID.name
            if course.courseTypeID:
                course_tye=course.courseTypeID.name
            if course.userID:
                if(course.userID.last_name and course.userID.first_name):
                    user=course.userID.last_name+" "+course.userID.first_name
                else:
                    user=course.userID.phone
            i["teacher_name"]=teacher
            i["department_name"]=department
            i["grade_name"]=grade
            i["course_type_name"]=course_tye
            i["lesson_name"]=lesson
            i["year_name"]=year
            i["user_name"]=user
            return Response(i,status=status.HTTP_200_OK)            

        else:
            page=request.query_params.get('page',None)
            dep=request.query_params.get('dep',None)
            grade=request.query_params.get('grade',None)
            course_type=request.query_params.get('course_type',None)
            lesson=request.query_params.get('lesson',None)
            courses=Course.objects.all()
            if dep:
                courses=courses.filter(departmentID=dep)
            if(grade):
                courses=courses.filter(gradeID=grade)
            if(course_type):
                courses=courses.filter(courseTypeID=course_type)
            if(lesson):
                courses=courses.filter(lessonID=lesson)
            if(page):
                page=int(page)-1
                courses=courses[page*9:page*9+9]
                
            ser = courseSerializer(courses, many=True)
            new_data=copy.deepcopy(ser.data)
            for i in new_data:
                course=get_object_or_404(Course,id=i["id"])
                teacher=""
                department=""
                grade=""
                course_tye=""
                lesson=""
                year=""
                user=""
                if course.teacherID:
                    if(course.teacherID.last_name and course.teacherID.first_name):
                        teacher=course.teacherID.last_name+" "+course.teacherID.first_name
                    else:
                        teacher=course.teacherID.phone
                if  course.departmentID:
                    department=course.departmentID.name
                if(course.gradeID):
                    grade=course.gradeID.name
                if course.courseTypeID:
                    course_tye=course.courseTypeID.name
                if course.userID:
                    if(course.userID.last_name and course.userID.first_name):
                        user=course.userID.last_name+" "+course.userID.first_name
                    else:
                        user=course.userID.phone
                i["teacher_name"]=teacher
                i["department_name"]=department
                i["grade_name"]=grade
                i["course_type_name"]=course_tye
                i["lesson_name"]=lesson
                i["year_name"]=year
                i["user_name"]=user

            return Response(new_data)  
    
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
        item=request.data
        block=BlocedStudent.objects.filter(studentID=item['studentID'],courseID=item['courseID'])
        if(block.count()!=0):
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
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        courseHomeWork = get_object_or_404(CourseHomeWork, id=id)
        ser = courseHomeWorkSerializer(courseHomeWork, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        courseDays = get_object_or_404(CourseDays, id=id)
        ser = courseTypeSerializer(courseDays, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        if 'id' not in request.data:
            return Response('id required', status=status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        courseType = get_object_or_404(CourseType, id=id)
        ser = courseTypeSerializer(courseType, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
        new_data=copy.deepcopy(ser.data)
        for i in new_data:
                course=get_object_or_404(Course,id=i["id"])
                teacher=""
                department=""
                grade=""
                course_tye=""
                lesson=""
                year=""
                user=""
                if course.teacherID:
                    if(course.teacherID.last_name and course.teacherID.first_name):
                        teacher=course.teacherID.last_name+" "+course.teacherID.first_name
                    else:
                        teacher=course.teacherID.phone
                if  course.departmentID:
                    department=course.departmentID.name
                if(course.gradeID):
                    grade=course.gradeID.name
                if course.courseTypeID:
                    course_tye=course.courseTypeID.name
                if course.userID:
                    if(course.userID.last_name and course.userID.first_name):
                        user=course.userID.last_name+" "+course.userID.first_name
                    else:
                        user=course.userID.phone
                i["teacher_name"]=teacher
                i["department_name"]=department
                i["grade_name"]=grade
                i["course_type_name"]=course_tye
                i["lesson_name"]=lesson
                i["year_name"]=year
                i["user_name"]=user
        return Response(new_data,status=status.HTTP_200_OK)

class coursegetHomeVIew(APIView):
    def get(self,request):
        id=request.query_params.get('id',None)
        if(id is  None):
            return Response("need query params",status=status.HTTP_400_BAD_REQUEST)
        hw=CourseHomeWork.objects.filter(courseID=id)
        hw_Ser=courseHomeWorkSerializer(hw,many=True)
        new_data=copy.deepcopy(hw_Ser.data)
        for i in new_data:
            course=get_object_or_404(Course,id=i["courseID"])
            i["course_name"]=course.name
        return Response(new_data,status=status.HTTP_200_OK)
        
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
        
class blockstudents(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        sid=request.query_params.get('student_id',None)
        cid=request.query_params.get('course_id',None)
        if(sid  is None and cid is None):
            return Response("need query params",status=status.HTTP_400_BAD_REQUEST)
        if(sid is not None and cid is  None):
            student=get_object_or_404(Student,pk=sid)
            blocked=BlocedStudent.objects.filter(studentID=student.pk)
            ser=blockstudentSerializer(blocked,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        if(sid is None and cid is not None):
            course=get_object_or_404(Course,id=cid)
            blocked=BlocedStudent.objects.filter(courseID=course.id)
            ser=blockstudentSerializer(blocked,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        blocked=BlocedStudent.objects.filter(courseID=cid,studentID=sid)
        ser=blockstudentSerializer(blocked,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)    
    def post(self,request):
        ans=[]
        for i in request.data:
            ser=blockstudentSerializer(data=i)
            if(ser.is_valid()):
                ser.save()
                ans.append(ser.data)
            else:
                ans.append(ser.errors)
        return Response(ans,status=status.HTTP_201_CREATED)
    def  delete(self,request):
        for i in request.data:
            block=get_object_or_404(BlocedStudent,id=i['id'])
            block.delete()
        return Response(status=status.HTTP_200_OK)    
        
class specificCoourseSes(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        id=request.query_params.get('c_id',None)
        if(id is None):
            return Response('need query param',status.HTTP_400_BAD_REQUEST)

        students=StudetCourse.objects.filter(courseID=id)
        ans=[]
        for x in students:
            data={
                'name':x.studentID.username,
                'phone':x.studentID.phone,
                'l_name':x.studentID.last_name,
                'grade':x.studentID.grade
            }
            ans.append(data)
        return Response(ans,status.HTTP_200_OK)    


