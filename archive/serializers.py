
from rest_framework import serializers
from .models import *

class archiveOfflineHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiveOfflineHeader
        fields = '__all__'  

class archiveFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiveFiles
        fields = '__all__'  
