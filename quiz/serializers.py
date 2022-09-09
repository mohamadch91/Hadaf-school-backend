from rest_framework import serializers
from .models import *

class quizHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = quizHeader
        fields = '__all__'  

class quizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = quizQuestion
        fields = '__all__'  


class studentQueezSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentQueez
        fields = '__all__'  
class totalquizHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = totalquizHeader
        fields = '__all__'

class totalquizSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = totalquizSubjects
        fields = '__all__'

class totalquizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = totalquizQuestion
        fields = '__all__'

class totalstudentQueezSerializer(serializers.ModelSerializer):
    class Meta:
        model = totalstudentQueez
        fields = '__all__'
            