from django.db import models
from Users.models import User,Trainer

"""Создем модель тренироки"""
class Workouts(models.Model):
    #План тренировок
    plan = models.CharField(max_length=255)

    #Дата тренировок
    due_date = models.DateField(auto_now=True)

    #Общее время
    total_time = models.PositiveIntegerField()

    #Общущение
    sensations = models.CharField(max_length=255)

    def __str__(self):
        return f"План тренировки {self.plan}, дата тренировки {self.due_date}, общее время {self.sensations} "



"""Создаем модель плана тренировки"""
class WorkoutPlan(models.Model):

    """Добавляем пользователя по первичному ключу в нашу модель плана тренировок с помощью класса User из приложения Users"""
    users = models.ForeignKey(User,on_delete=models.CASCADE)

    #Тренер
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE)

    #Название
    title = models.CharField(max_length=255)

    #Цель
    target = models.TextField(blank=True)

    def __str__(self):
        return f" Пользователю {str(self.users)} назначен тренер {str(self.trainer)} "