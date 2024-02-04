from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class FileSerializer(ModelSerializer):
    # processed = serializers.HiddenField(default=True)

    class Meta:
        model = File
        fields = ('file', 'uploaded_at')


class AllFileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'uploaded_at', 'processed')
