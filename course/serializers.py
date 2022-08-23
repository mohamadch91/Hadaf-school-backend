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

class archiveOfflineHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiveOfflineHeader
        fields = '__all__'  
