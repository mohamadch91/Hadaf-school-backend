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
    permission_classes=(IsAuthenticated,)
   
    def put (self,request):
        if('id' not in request.data):
            return Response("neeed id ",status=status.HTTP_400_BAD_REQUEST)
        if('type' not in request.data ):
            return Response("neeed type",status=status.HTTP_400_BAD_REQUEST)
        type=request.data["type"]
        id=request.data["id"]
        if(type=="user"):
            user=get_object_or_404(User,pk=id)
            ser=updateUserSerilizer(user,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_202_ACCEPTED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        if(type=="student"):
            user=get_object_or_404(Student,pk=id)
            ser=updateStudentSerializer(user,data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data,status=status.HTTP_202_ACCEPTED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        if(type=="teacher"):
            user=get_object_or_404(Teacher,pk=id)
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
        if(type==None):
            users=User.objects.all()
            ser=UserSerializer(users,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        if(type=='student'):
            users=Student.objects.all()
            ser=StudentSerializer(users,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        if(type=='teacher'):
            users=Teacher.objects.all()
            ser=TeacherSerializer(users,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)


class OTPView(APIView):
    def get(self, request):
        serializer = RequestOTPSerializer(data=request.query_params)
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
        
        query = User.objects.filter(username=otp['receiver'])
        if query.exists():
            created = False
            user = query.first()
        else:
            user = User.objects.create(username=otp['receiver'] )
            created = True

        refresh = RefreshToken.for_user(user)

        return ObtainTokenSerializer({
            'refresh': str(refresh),
            'token': str(refresh.access_token),
            'created':created
        }).data
