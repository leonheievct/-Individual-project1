from django.db import models
from Users.models import User


"""Создаем модель продукта питания """
class FoodItem(models.Model):
    """Передаем атрибуты нашей модели"""
    title = models.CharField(max_length=50)
    calories = models.PositiveIntegerField()

    #Белки
    squirrels = models.PositiveIntegerField()
    #Жиры
    fats = models.PositiveIntegerField()
    #Углеводы
    carbohydrates = models.PositiveIntegerField()

    def __str__(self):
        return self.title


"""Создаем модель журнала приема пищи"""
class FoodLog(models.Model):
    """Передаем атрибуты нашей модели по первичному ключу из локального класса и класса из другого приложения Users"""
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    #Продукт питания
    food_item = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    #Количество 
    quantity = models.PositiveIntegerField()
    #Прием пищи
    meal = models.CharField(max_length=2,choices=[('one','1'),('two','2'),('three','3')],default='one')
    data = models.DateField(auto_now=True)