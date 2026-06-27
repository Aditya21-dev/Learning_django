from rest_framework import serializers
from .models import User

class UserSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    email = serializers.EmailField()
    contact = serializers.CharField(max_length=10)
    city = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
