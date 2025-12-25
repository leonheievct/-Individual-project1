from .models import UserProfile
from rest_framework import serializers


class SimpleUserSerializer(serializers.ModelSerializer):
    """Передаем только базовые поля пользователя"""
    class Meta:
        model = UserProfile
        fields = '__all__'