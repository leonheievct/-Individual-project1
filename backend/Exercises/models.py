from django.db import models

"""Создаем модель упражнений"""
class Exercise(models.Model):

    title = models.CharField(max_length=70,verbose_name='Название')
    discription = models.TextField(blank=True,verbose_name='Описание')

    #Группа мыщц
    muscle_group = models.CharField(max_length=50,choices= [
        ('CHEST', 'Грудь'),
        ('BACK', 'Спина'),
        ('LEGS', 'Ноги'),
        ('SHOULDERS', 'Плечи'),
        ('ARMS', 'Руки'),
        ('CORE', 'Пресс'),
        ('CARDIO', 'Кардио'),
        ('FULL_BODY', 'Все тело'),
    ],verbose_name='Группа мыщц',default='FULL_BODY')

    #Оборудование
    equipment = models.CharField(max_length=50,choices= [
        ('BARBELL', 'Штанга'),
        ('DUMBBELL', 'Гантели'),
        ('MACHINE', 'Тренажер'),
        ('BODYWEIGHT', 'Собственный вес'),
        ('CABLE', 'Тросы'),
        ('KETTLEBELL', 'Гири'),
        ('RESISTANCE_BAND', 'Эспандер'),
        ('OTHER', 'Другое'),
    ],verbose_name='Оборудование',default='BODYWEIGHT')

    def __str__(self):
        return self.title
     




