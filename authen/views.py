import http
from re import L
from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from authen.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from django.shortcuts import get_object_or_404
from itertools import chain
import copy
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class StudentRegisterView(generics.CreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class=StudentSerializer
    queryset =Student.objects.all()
    def post(self,request):
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response (ser.errors,status=status.HTTP_400_BAD_REQUEST)    


class TeacherRegisterView(generics.CreateAPIView):
    serializer_class=TeacherSerializer
    permission_classes=(IsAuthenticated,)

    queryset =Teacher.objects.all()
    def post(self,request):
        ser=TeacherSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response (ser.errors,status=status.HTTP_400_BAD_REQUEST)
class UserRegisterView(generics.CreateAPIView):
    serializer_class=UserSerializer
    permission_classes=(IsAuthenticated,)
    queryset =User.objects.all()
    def post(self,request):
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response (ser.errors,status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer   
class UpdateProfileView(APIView):
    # permission_classes=(IsAuthenticated,)
   
    def put (self,request):
        if('phone' not in request.data):
            return Response("neeed phone ",status=status.HTTP_400_BAD_REQUEST)
        if('type' not in request.data ):
            return Response("neeed type",status=status.HTTP_400_BAD_REQUEST)
        type=request.data["type"]
        phone=request.data["phone"]
        if(type=="user"):
            user=get_object_or_404(User,phone=phone)
            ser=updateUserSerilizer(user,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_202_ACCEPTED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        if(type=="student"):
            user=get_object_or_404(Student,phone=phone)
            ser=updateStudentSerializer(user,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_202_ACCEPTED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        if(type=="teacher"):
            user=get_object_or_404(Teacher,phone=phone)
            ser=updateTeacherSerializer(user,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_202_ACCEPTED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)        



class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)            

class UserListView(generics.ListAPIView):
    permission_classes=(IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        type=request.query_params.get('type',None)
        id=request.query_params.get('id',None)
        if(type==None):
            students=Student.objects.values_list('pk',flat=True)
            teachers=Teacher.objects.values_list('pk',flat=True)
            all=list(chain(students, teachers))
            users=User.objects.exclude(pk__in=all)
            if(id is not None):
                users=users.filter(pk=id)
            ser=UserSerializer(users,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        if(type=='student'):
            users=Student.objects.all()
            if(id is not None):
                users=users.filter(pk=id)
            ser=StudentSerializer(users,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        if(type=='teacher'):
            users=Teacher.objects.all()
            if(id is not None):
                users=users.filter(pk=id)
            ser=TeacherSerializer(users,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)


class OTPViewLogin(APIView):
    def get(self, request):
        
        serializer = RequestOTPSerializer(data=request.query_params)
        user=get_object_or_404(User,phone=request.query_params.get('receiver'))
        if serializer.is_valid():
            data = serializer.validated_data
            otp = OTPRequest.objects.generate(data)
            return Response(data=RequestOTPResponseSerializer(otp).data,status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors)
    def post(self, request):
        serializer = VerifyOtpRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if OTPRequest.objects.is_valid(data['receiver'], data['request_id'], data['password']):
                return Response(self._handle_login(data))
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors)

    def _handle_login(self, otp):
        
        query = User.objects.filter(phone=otp['receiver'])
        if query.exists():
            created = False
            user = query.first()

        refresh = RefreshToken.for_user(user)

        return ObtainTokenSerializer({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'created':created
        }).data
class OTPViewRegister(APIView):
    def get(self, request):
        
        serializer = RequestOTPSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            otp = OTPRequest.objects.generate(data)
            return Response(data=RequestOTPResponseSerializer(otp).data,status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors)
    def post(self, request):
        if('type' not in request.data ):
            return Response("neeed type",status=status.HTTP_400_BAD_REQUEST)#
        serializer = VerifyOtpRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if OTPRequest.objects.is_valid(data['receiver'], data['request_id'], data['password']):
                return Response(self._handle_login(data,request))
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors)

    def _handle_login(self, otp,request):
        type=request.data["type"]
        if(type=="student"):
            try:
                s=get_object_or_404(Student,phone=otp['receiver'])
                return Response("phone already exists",status=status.HTTP_400_BAD_REQUEST)
            except:    
                user = Student.objects.create(phone=otp['receiver'] )
                created = True
                refresh = RefreshToken.for_user(user)
        elif(type=="teacher"):
            try:
                s=get_object_or_404(Teacher,phone=otp['receiver'])
                return Response("phone already exists",status=status.HTTP_400_BAD_REQUEST)
            except:    
                user =  Teacher.objects.create(phone=otp['receiver'] )
                created = True
                refresh = RefreshToken.for_user(user)
    
        else:
            try:
                s=get_object_or_404(User,phone=otp['receiver'])
                return Response("phone already exists",status=status.HTTP_400_BAD_REQUEST)
            except:
                    
                user = User.objects.create(phone=otp['receiver'] )
                created = True
                refresh = RefreshToken.for_user(user)

        return ObtainTokenSerializer({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'created':created
        }).data

class deleteUser(APIView):
    permission_classes=(IsAuthenticated,)

    def post(self,request):
        user=get_object_or_404(User,pk=request.data["id"])
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class changePasswordViews(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self,request):
        id=request.data["id"]
        user=get_object_or_404(User,pk=id)
        if not user.check_password(request.data["old"]):
            return Response("old password is incorrect",status=status.HTTP_400_BAD_REQUEST)
        user.set_password(request.data["password"])
        user.save()
        return Response("password change succesfully",status=status.HTTP_202_ACCEPTED)

            

class adminLoginbyUserView(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self,request):
        id=request.data["id"]
        user=get_object_or_404(User,pk=id)
        refresh = RefreshToken.for_user(user)
        ser= ObtainTokenSerializer({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'created':False
        }).data
        return Response(ser,status=status.HTTP_202_ACCEPTED)

class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class CurruptedView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        school=request.query_params.get('school')
        parentName=request.query_params.get('parentName')
        parentNationalCode=request.query_params.get('parentNationalCode')
        pbirthday=request.query_params.get('pbirthday')
        peducation=request.query_params.get('peducation')
        pjob=request.query_params.get('pjob')
        address=request.query_params.get('address')
        students=Student.objects.all()
        if(school is not None):
            students=students.filter(school=None) |students.filter(school="")
        if(parentName is not None):
            students=students.filter(parentName=None)|students.filter(parentName="")
        if(parentNationalCode is not None):
            students=students.filter(parentNationalCode=None)|students.filter(parentNationalCode="")
        if(pbirthday is not None):
            students=students.filter(pbirthday=None)|students.filter(pbirthday="")
        if(peducation is not None):
            students=students.filter(peducation=None)|students.filter(peducation="")
        if(pjob is not None):
            students=students.filter(pjob=None)|students.filter(pjob="")
        if(address is not None):
            students=students.filter(address=None)|students.filter(address="")
        serializer = StudentSerializer(students,many=True)
        new_copy=copy.deepcopy(serializer.data)
        for i in new_copy:
            grades=""
            if(i["grade"] is not None):
                grades=get_object_or_404(grade,id=i["grade"]).name
            i["gradeName"]=grades
            dep=""
            if(i["department"] is not None):
                dep=get_object_or_404(department,id=i["department"]).name
            i["departmentName"]=dep              
        return Response(data=new_copy,status=status.HTTP_200_OK)

class loginUserView(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self,request):
        user=get_object_or_404(User,pk=request.data["id"])
        refresh = RefreshToken.for_user(user)
        ser= ObtainTokenSerializer({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'created':False
        }).data
        return Response(ser,status=status.HTTP_202_ACCEPTED)
        