from rest_framework import serializers
from .models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    muscle_group = serializers.CharField(
        source='Exercise.muscle_group',
        read_only=True
    )
    equipment = serializers.CharField(
        source='Exercise.equipment',
        read_only=True
    )
    
    class Meta:
        model = Exercise
        fields = [
            'id',
            'name',
            'description',
            'muscle_group',
            'muscle_group_display',
            'equipment',
            'equipment_display',
            'created_at',
            'updated_at'
        ]