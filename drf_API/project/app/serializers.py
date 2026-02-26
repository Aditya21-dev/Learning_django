from rest_framework import serializers

class UserSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=40)
    email=serializers.EmailField(max_length=40)
    contact=serializers.IntegerField()
    city=serializers.IntegerField()