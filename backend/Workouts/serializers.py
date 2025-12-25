from rest_framework import serializers
from .models import WorkoutPlan, Workouts, Set
from Exercises.serializers import ExerciseSerializer

class SetSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    exercise_id = serializers.CharField(
        source='exercise',
        write_only=True
    )
    
    class Meta:
        model = Set
        fields = [
            'workout_session',
            'exercise',
            'exercise_id',
            'weight',
            'repetitions',
            'set_number',

        ]

class WorkoutSessionSerializer(serializers.ModelSerializer):
    sets = SetSerializer(read_only=True)
    feeling_display = serializers.CharField(
        source='Workouts.feeling',
        read_only=True
    )
    
    class Meta:
        model = Workouts
        fields = [
            'workout_plan',
            'due_date',
            'total_time',
            'feeling',
            'feeling_display',
            'sets',
        ]

class WorkoutSessionDetailSerializer(serializers.ModelSerializer):
    sets = SetSerializer(read_only=True)
    feeling_display = serializers.CharField(
        source='Workouts.feeling',
        read_only=True
    )
    
    class Meta:
        model = Workouts
        fields = [
            'workout_plan',
            'due_date',
            'total_time',
            'feeling',
            'feeling_display',
            'sets',
        ]

class WorkoutPlanSerializer(serializers.ModelSerializer):
    sessions = WorkoutSessionSerializer(read_only=True)
    goal_display = serializers.CharField(
        source='WorkoutPlan.goal',
        read_only=True
    )
    user_username = serializers.CharField(
        source='user.username',
        read_only=True
    )
    trainer_username = serializers.CharField(
        source='trainer.username',
        read_only=True,
    )
    
    class Meta:
        model = WorkoutPlan
        fields = [
            'users',
            'user_username',
            'trainer',
            'trainer_username',
            'title'
            'goal',
            'goal_display',
        ]

class WorkoutPlanDetailSerializer(serializers.ModelSerializer):
    sessions = WorkoutSessionDetailSerializer(read_only=True)
    goal_display = serializers.CharField(
        source='WorkoutPlan.goal',
        read_only=True
    )
    user_username = serializers.CharField(
        source='user.username',
        read_only=True
    )
    trainer_username = serializers.CharField(
        source='trainer.username',
        read_only=True,
        allow_null=True
    )
    
    class Meta:
        model = WorkoutPlan
        fields =[
            'users',
            'user_username',
            'trainer',
            'trainer_username',
            'title'
            'goal',
            'goal_display',
        ]
