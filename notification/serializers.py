from dataclasses import field
from rest_framework import serializers
from .models import *



class notificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = notification
        fields = '__all__'

class studentNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentNotification
        fields = '__all__'

class studentNotificationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentNotificationRead
        fields = '__all__'
        