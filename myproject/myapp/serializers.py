from rest_framework import serializers
from .models import User, Photo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'file', 'fileName', 'fileType', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        file = validated_data.get('file')
        validated_data['fileName'] = file.name
        validated_data['fileType'] = file.content_type
        return super().create(validated_data)