from rest_framework import serializers
from api.models import Datasets

class DatasetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)

    def create(self, validated_data):
        return Datasets.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)

        instance.save()

        return instance