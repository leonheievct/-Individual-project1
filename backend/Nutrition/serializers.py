from rest_framework import serializers
from .models import FoodItem, FoodLog

class FoodItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FoodItem
        fields = [
            'id',
            'name',
            'calories',
            'protein',
            'fat',
            'carbs',
        ]

class FoodLogSerializer(serializers.ModelSerializer):
    food_item = FoodItemSerializer(read_only=True)
    food_item_id = serializers.CharField(
        source='FoodLog.food_item',read_only=True
    )
    meal_type_display = serializers.CharField(
        source='FoodLog.meal_type',
        read_only=True
    )
    total_nutrition = serializers.SerializerMethodField()
    user_username = serializers.CharField(
        source='user.username',
        read_only=True
    )
    
    class Meta:
        model = FoodLog
        fields = [
            'id',
            'user',
            'user_username',
            'food_item',
            'food_item_id',
            'quantity',
            'meal_type',
            'meal_type_display',
            'date',


        ]