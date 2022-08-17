from dataclasses import field, fields
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
        fields = ['pk','phone','password','birth','national_code','role','first_name','last_name','created_at','updated_at','picture']
        extra_kwargs = {'password': {'write_only': True}}
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
        fields = ['pk','phone','grade','department','birth','password','national_code','role','first_name','last_name','created_at','updated_at','picture','gpaverage','disipcline','school','parentName','parentNationalCode','pbirthday','peducation','pjob','address']
        extra_kwargs = {'password': {'write_only': True}}
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
        fields = ['pk','phone','password','birth','national_code','role','first_name','last_name','created_at','updated_at','picture']                
        extra_kwargs = {'password': {'write_only': True}}
    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)   
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
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
