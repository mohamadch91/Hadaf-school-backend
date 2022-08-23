from dataclasses import field
from rest_framework import serializers
from .models import *




class discountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'  

class discountCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCourse
        fields = '__all__'  
