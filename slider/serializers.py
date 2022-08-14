
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'picture', 'link', 'active', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'picture', 'title', 'active', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')