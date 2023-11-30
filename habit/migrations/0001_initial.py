# Generated by Django 4.2.7 on 2023-11-19 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='Место действия')),
                ('time', models.TimeField(verbose_name='Время, когда необходимо выполнять действие')),
                ('action', models.CharField(max_length=150, verbose_name='Действия')),
                ('period', models.CharField(choices=[('Daily', 'Ежедневно'), ('Weekly', 'Еженедельно'), ('Monthly', 'Ежемесячно')], default='Daily', max_length=10, verbose_name='Периодичность')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
        migrations.CreateModel(
            name='PleasantHabit',
            fields=[
                ('habit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='habit.habit')),
            ],
            options={
                'verbose_name': 'Приятная привычка',
                'verbose_name_plural': 'Приятные привычки',
            },
            bases=('habit.habit',),
        ),
        migrations.CreateModel(
            name='UsefulHabit',
            fields=[
                ('habit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='habit.habit')),
                ('reward', models.CharField(blank=True, max_length=255, verbose_name='Вознаграждение')),
                ('time_required', models.PositiveIntegerField(default=2, verbose_name='Время на выполнение (в минутах)')),
            ],
            options={
                'verbose_name': 'Полезная привычка',
                'verbose_name_plural': 'Полезные привычки',
            },
            bases=('habit.habit',),
        ),
    ]