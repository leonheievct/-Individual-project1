from django.db import models
from users.models import UserProfile


"""Создаем модель продукта питания """
class FoodItem(models.Model):

    """Передаем атрибуты нашей модели"""

    name = models.CharField(max_length=200, verbose_name='Название')

    #Калорий
    calories = models.FloatField(verbose_name='Калории (ккал)')

    #Белки
    protein = models.FloatField(verbose_name='Белки (г)')

    #Жиры
    fat = models.FloatField(verbose_name='Жиры (г)')

    #Углеводы
    carbs = models.FloatField(verbose_name='Углеводы (г)')

    def __str__(self):
        return self.name



"""Создаем модель журнала приема пищи"""

class FoodLog(models.Model):

    """Передаем атрибуты нашей модели по первичному ключу из локального класса и класса из другого приложения Users"""

    users = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    #Продукт питания
    food_item = models.ForeignKey(FoodItem,on_delete=models.CASCADE)

    #Количество 
    quantity = models.FloatField(verbose_name='Количество (г)')

    #Прием пищи
    meal_type = models.CharField(max_length=20,choices= [
        ('BREAKFAST', 'Завтрак'),
        ('LUNCH', 'Обед'),
        ('DINNER', 'Ужин'),
        ('SNACK', 'Перекус'),
        ('PRE_WORKOUT', 'Перед тренировкой'),
        ('POST_WORKOUT', 'После тренировки'),
    ],verbose_name='Прием пищи')

    #Дата
    date = models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.users.username} - {self.food_item.name} - {self.date}"