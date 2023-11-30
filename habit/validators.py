from rest_framework import serializers


class ValidateReward:
    def __init__(self, reward, related_habit):
        self.reward = reward
        self.related_habit = related_habit

    def __call__(self, value):
        reward = dict(value).get(self.reward)
        related_habit = dict(value).get(self.related_habit)

        if reward is None and related_habit is None:
            raise serializers.ValidationError('Выберите награду или приятную привычку')
        elif reward and related_habit:
            raise serializers.ValidationError('Выбрать можно что-то одно - награда или приятная привычка')


class ValidateTimeRequired:
    def __init__(self, time_required):
        self.time_required = time_required

    def __call__(self, value):
        if 'time_required' in dict(value):
            time_required = dict(value).get(self.time_required)
            if time_required > 120:
                raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд')


class ValidatePeriod:
    def __init__(self, period):
        self.period = period

    def __call__(self, value):
        if 'period' in dict(value):
            period = dict(value).get(self.period)
            if period not in ['weekly', 'daily']:
                raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')