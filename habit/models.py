from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    PERIOD_CHOICES = [
        ('Daily', 'Ежедневно'),
        ('Weekly', 'Еженедельно'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                             **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место действия')
    time = models.DateTimeField(verbose_name='Время, когда необходимо выполнять действие')
    action = models.CharField(max_length=150, verbose_name='Действия')
    period = models.CharField(default='Daily', max_length=10, choices=PERIOD_CHOICES, verbose_name='Периодичность')
    time_required = models.PositiveIntegerField(default=60, verbose_name='Время на выполнение, с')

    is_public = models.BooleanField(default='False', verbose_name='Публичная ли запись')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}.'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'


class PleasantHabit(Habit):

    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'


class UsefulHabit(Habit):
    related_habit = models.ForeignKey(PleasantHabit, on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name='Связанная привычка')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение', **NULLABLE)

    class Meta:
        verbose_name = 'Полезная привычка'
        verbose_name_plural = 'Полезные привычки'
