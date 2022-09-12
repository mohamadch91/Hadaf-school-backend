from rest_framework import serializers
from .models import *

class buySerializer(serializers.ModelSerializer):
    class Meta:
        model = buy
        fields = '__all__'
        