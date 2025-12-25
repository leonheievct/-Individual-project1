from django.db import models
from Users.models import User
from Exercises.models import Exercise


"""Создаем модель плана тренировки"""
class WorkoutPlan(models.Model):

    """Добавляем пользователя по первичному ключу в нашу модель плана тренировок с помощью класса User из приложения Users"""
    users = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Пользователь')

    #Тренер
    trainer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Тренер')

    #Название
    title = models.CharField(max_length=255,verbose_name='Название плана')

    #Цель
    goal = models.CharField(max_length=20,choices= [
        ('STRENGTH', 'Сила'),
        ('HYPERTROPHY', 'Набор массы'),
        ('ENDURANCE', 'Выносливость'),
        ('FAT_LOSS', 'Сжигание жира'),
        ('MAINTENANCE', 'Поддержание формы'),
        ('REHAB', 'Реабилитация'),
    ],verbose_name='Цель')

    def __str__(self):
        return f" Пользователю {str(self.users)} назначен тренер {str(self.trainer)}, цель: {self.goal} "



"""Создем модель тренироки"""
class Workouts(models.Model):
    
    #План тренировок
    workouts_plan = models.ForeignKey(WorkoutPlan,on_delete=models.CASCADE,verbose_name='План тренировки')

    #Дата тренировок
    due_date = models.DateField(auto_now=True,verbose_name='Дата выполнения')

    #Общее время
    total_time = models.PositiveIntegerField()

    #Ощущение
    feeling = models.CharField(max_length=40,choices= [
        ('GREAT', 'Отлично'),
        ('GOOD', 'Хорошо'),
        ('NORMAL', 'Нормально'),
        ('BAD', 'Плохо'),
        ('TERRIBLE', 'Ужасно'),
    ],default='NORMAL')

    def __str__(self):
        return f"План тренировки {str(self.workouts_plan)}, дата тренировки {str(self.due_date)}, общее время {self.total_time} "



""" Создаем набор из наших моделей Workouts """

class Set(models.Model):

    """Создаем атрибуты (сессий,упражнения) по первичному ключу используя локальный класс и клас Workouts другого приложения"""
    workout_session = models.ForeignKey(Workouts,on_delete=models.CASCADE,verbose_name='Тренировка')
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE,verbose_name='Упражнение')

    #Вес
    weight = models.FloatField(null=True,blank=True,verbose_name='Вес (кг)')

    #Повторения
    repetitions = models.PositiveIntegerField()

    #Номер подхода
    set_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exercise.title} - Подход {self.set_number}"