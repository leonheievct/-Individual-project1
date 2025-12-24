from django.db import models
from Workouts.models import Workouts

"""Создаем модель упражнений"""
class Exercise(models.Model):
    title = models.CharField(max_length=70)
    discription = models.TextField(blank=True)

    #Группа мыщц
    muscle_group = models.CharField(max_length=50)

    #Оборудование
    equipment = models.CharField(max_length=50)

    def __str__(self):
        return self.title
     
""" Создаем набор из наших моделей Workouts,WorkoutPlan """
class Set(models.Model):

    """Создаем атрибуты (сессий,упражнения) по первичному ключу используя локальный класс и клас Workouts другого приложения"""
    session = models.ForeignKey(Workouts,on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE)

