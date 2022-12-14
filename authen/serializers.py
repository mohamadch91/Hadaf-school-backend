from dataclasses import field, fields
from os import access
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from authen.models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth.hashers import make_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['pk','phone','birth','national_code','role','first_name','last_name','created_at','updated_at','picture']
    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)   
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['pk','phone','grade','department','birth','national_code','role','first_name','last_name','created_at','updated_at','picture','gpaverage','disipcline','school','parentName','parentNationalCode','pbirthday','peducation','pjob','address']
    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)    
                
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk','phone','birth','national_code','role','first_name','last_name','created_at','updated_at','picture']                
    # def validate_password(self, value: str) -> str:
    #     """
    #     Hash value passed by user.

    #     :param value: password of a user
    #     :return: a hashed version of the password
    #     """
    #     return make_password(value)   
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields= '__all__'  

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password')

  

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance        
class updateUserSerilizer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['pk','phone','birth','national_code','role','first_name','last_name','created_at','updated_at','picture']                

class updateTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['pk','phone','birth','national_code','role','first_name','last_name','created_at','updated_at','picture']

class updateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['pk','phone','grade','department','birth','national_code','role','first_name','last_name','created_at','updated_at','picture','gpaverage','disipcline','school','parentName','parentNationalCode','pbirthday','peducation','pjob','address']

class requestOTPSerializer(serializers.Serializer):
    reciever=serializers.IntegerField(allow_null=False)
        
class RequestOTPSerializer(serializers.Serializer):
    receiver = serializers.CharField( allow_null=False)


class RequestOTPResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPRequest
        fields =['request_id']

class VerifyOtpRequestSerializer(serializers.Serializer):
    request_id = serializers.UUIDField(allow_null=False)
    password = serializers.CharField(allow_null=False)
    receiver = serializers.CharField( allow_null=False)

class ObtainTokenSerializer(serializers.Serializer):
    access = serializers.CharField( allow_null=False)
    refresh = serializers.CharField( allow_null=False)
    created = serializers.BooleanField()

class userIpSerializer(serializers.ModelSerializer):
    class Meta:
        model = userIp
        fields = '__all__'

