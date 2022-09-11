from dataclasses import field
from rest_framework import serializers
from .models import *

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class studentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudetCourse
        fields = '__all__'

class courseHomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseHomeWork
        fields = '__all__'             

class courseDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDays
        fields = '__all__'  

class courseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = '__all__'  


class blockstudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlocedStudent
        fields = '__all__'

class homeworkanswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeworkanswer
        fields = '__all__'