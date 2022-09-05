from rest_framework import serializers
from .models import *

class normalPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = normalPackage
        fields = '__all__'

class normalPackageCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = normalPackageCourse
        fields = '__all__'


class timingPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = timingPackage
        fields = '__all__'

class timingPackageCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = timingPackageCourse
        fields = '__all__'

class studentPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentPackage
        fields = '__all__'

class studentPackageCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentPackageCourse
        fields = '__all__'

class studentPackageDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentPackageDiscount
        fields = '__all__'