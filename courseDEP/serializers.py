from rest_framework import serializers
from .models import *

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = '__all__'


class gradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = grade
        fields = '__all__'

class lessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = lessons
        fields = '__all__'

class daysSerializer(serializers.ModelSerializer):
    class Meta:
        model = days
        fields = '__all__'

class   yearSerializer(serializers.ModelSerializer):
    class Meta:
        model = year
        fields = '__all__'
class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = '__all__'        