from datetime import datetime, timedelta
from celery import shared_task
from habit.models import Habit
from config.settings import BOT_API
import requests


@shared_task
def notification():
    current_time = datetime.now().time().replace(second=0, microsecond=0)

    # Обработка ежедневных привычек
    daily_habits = Habit.objects.filter(period='Daily')
    for habit in daily_habits:
        habit_time = habit.time.time().replace(second=0, microsecond=0)
        if habit_time >= current_time:
            send_notification(habit)
            update_next_notification_time(habit, timedelta(days=1))

    # Обработка еженедельных привычек
    weekly_habits = Habit.objects.filter(period='Weekly')
    for habit in weekly_habits:
        habit_time = habit.time.time().replace(second=0, microsecond=0)
        if habit_time >= current_time and habit.day_of_week == datetime.now().weekday():
            send_notification(habit)
            update_next_notification_time(habit, timedelta(weeks=1))


def send_notification(habit):
    message = f'Я буду {habit.action} в {habit.place} в {habit.time}'
    url_address = f'https://api.telegram.org/bot{BOT_API}/sendMessage?chat_id={habit.user.telegram_id}&text={message}'
    requests.get(url_address)


def update_next_notification_time(habit, delta):
    habit.next_notification += delta
    habit.save()