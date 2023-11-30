from rest_framework import serializers

from habit.models import UsefulHabit, PleasantHabit, Habit
from habit.validators import ValidateTimeRequired, ValidateReward


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class UsefulHabitSerializer(HabitSerializer):
    class Meta:
        model = UsefulHabit
        fields = '__all__'


class CreateUsefulHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulHabit
        exclude = ('user',)
        validators = [
            ValidateTimeRequired(time_required='time_required'),
            ValidateReward(reward='reward', related_habit='related_habit'),
        ]


class UpdateUsefulHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulHabit
        fields = "__all__"
        validators = [
            ValidateTimeRequired(
                time_required='time_required'
            )
        ]

    def validate(self, data):
        if 'related_habit' in dict(data) and data['related_habit'] and self.instance.reward:
            data['reward'] = None
            return data
        elif 'reward' in dict(data) and data['reward'] and self.instance.related_habit:
            data['related_habit'] = None
            return data
        else:
            return data

    def update(self, instance, validated_data):
        if 'related_habit' in validated_data and validated_data['related_habit'] and instance.reward:
            validated_data['reward'] = None
        elif 'reward' in validated_data and validated_data['reward'] and instance.related_habit:
            validated_data['related_habit'] = None

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class PleasantHabitSerializer(HabitSerializer):
    class Meta(HabitSerializer.Meta):
        model = PleasantHabit
        fields = '__all__'
        validators = [
            ValidateTimeRequired(
                time_required='time_required'
            )
        ]


class CreatePleasantHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PleasantHabit
        exclude = ('user',)
        validators = [
            ValidateTimeRequired(
                time_required='time_required'
            ),
        ]


class PublicHabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"