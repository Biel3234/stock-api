from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            'name',
            'email',
            'password'
        ]

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            'name',
            'email',
        ]