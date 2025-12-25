from .models import User
from rest_framework import serializers


class SimpleUserSerializer(serializers.ModelSerializer):
    """Передаем только базовые поля пользователя"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']