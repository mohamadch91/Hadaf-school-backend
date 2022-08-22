from dataclasses import field
from rest_framework import serializers
from .models import *

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class studentCourseSerializer(serializers.ModelSerializer):
    class Mete:
        model = StudetCourse
        field = '__all__'
               