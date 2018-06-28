from rest_framework import serializers
from .models import *

class PipelinesSerializer(serializers.Serializer):

    pipelines = serializers.JSONField()
    

class SessionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    
    email = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(max_length=1000, default = "")
    pipeline = serializers.CharField(max_length=100)
    config = serializers.JSONField()
    observation = serializers.CharField(max_length=1000)

    status = serializers.CharField(max_length = 20, default = "unknown")
    pipeline_version = serializers.CharField(max_length=100, default = "", read_only=True)
    pipeline_respone = serializers.CharField(max_length = 1000, default = "")
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Session.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.description = validated_data.get('description', instance.description)
        instance.pipeline = validated_data.get('pipeline', instance.pipeline)
        instance.config = validated_data.get('config', instance.config)
        instance.observation = validated_data.get('observation', instance.observation)

        instance.pipeline_version = validated_data.get('pipeline_version', instance.pipeline_version)
        instance.status = validated_data.get('status', instance.status)
        instance.pipeline_response = validated_data.get('pipeline_response', instance.pipeline_response)
        
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.date_modified = validated_data.get('date_modified', instance.date_modified)

        instance.save()
        return instance