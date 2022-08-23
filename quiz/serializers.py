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
