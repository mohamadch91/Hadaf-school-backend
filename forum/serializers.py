from rest_framework import serializers
from .models import *

class ForumHeaderSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = ForumHeader
        fields = '__all__'  

class ForumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumDetail
        fields = '__all__'  
