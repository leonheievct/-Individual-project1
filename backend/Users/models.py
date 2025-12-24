from django.db import models
from django.contrib.auth.models import AbstractUser


""" Создаем модель пользователя для нашего трекера используя AbstractUser """
class User(AbstractUser):
    phone = models.CharField(max_length=12)
    post = models.EmailField()
    create_at = models.DateTimeField(auto_now_add=True)

""" Создаем модель тренера для наших тренировок """
class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    #Стаж работы 
    work_experience = models.DateField(auto_now=True)