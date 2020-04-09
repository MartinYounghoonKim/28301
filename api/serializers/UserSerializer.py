"""
회원 정보 Serilizer
"""

from rest_framework import serializers
from ..models import User, DutyType

class UserSerializer(serializers.Serializer):
    """
    회원 정보 Serializer
    """
    userId = serializers.CharField(required=True, allow_blank=False, max_length=32)
    userName = serializers.CharField(required=True, allow_blank=False, max_length=32)
    password = serializers.CharField(required=True, allow_blank=False, max_length=128)
    duty = serializers.CharField(required=True, allow_blank=False, max_length=3)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.userName = validated_data.get('userName', instance.userName)
        instance.password = validated_data.get('password', instance.password)
        instance.duty = validated_data.get('duty', instance.duty)
        return instance
