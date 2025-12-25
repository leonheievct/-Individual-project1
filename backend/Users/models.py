from django.db import models
from django.contrib.auth.models import AbstractUser


""" Создаем модель пользователя для нашего трекера используя AbstractUser """
class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    user_type = models.CharField(
        max_length=10,
        choices=[
        ('USER', 'Пользователь'),
        ('TRAINER', 'Тренер'),
    ],
    default='USER',
    verbose_name='Тип пользователя'
    )
  
    height = models.FloatField(null=True, blank=True, verbose_name='Рост (см)')
    weight = models.FloatField(null=True, blank=True, verbose_name='Вес (кг)')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    bio = models.TextField(blank=True, verbose_name='О себе')
    fitness_goals = models.TextField(blank=True, verbose_name='Цели')



