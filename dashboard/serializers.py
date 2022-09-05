from rest_framework import serializers
from .models import *

class basketSerializer(serializers.ModelSerializer):
    class Meta:
        model = basket
        fields = '__all__'

class walletSerializer(serializers.ModelSerializer):
    class Meta:
        model = wallet
        fields = '__all__'