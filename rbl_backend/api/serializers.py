from rest_framework import serializers
from api.models import UsersModel

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 100)

    def create(self, validated_data):
        return UsersModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)

        instance.save()

        return instance