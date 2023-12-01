Habit Tracker
Добро пожаловать в Habit Tracker - веб-приложение для отслеживания полезных привычек!
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и
искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер
полезных привычек.

## Начало работы

1. Клонируйте репозиторий на свой компьютер:
    - git clone https://github.com/KapetanVodichka/drf_course.git

2. Создайте виртуальное окружение (рекомендуется):
    - python -m venv venv

3. Активируйте виртуальное окружение:
   **Windows:**
        - venv\Scripts\activate

   **Linux/Mac:**
        - source venv/bin/activate

4. Установите зависимости:
    - pip install -r requirements.txt

5. Создайте файл env. по шаблону .env.sample в корневой директории проекта и заполните данные для настройки проекта.

6. Создайте базу данных по командам:

    - psql -U postgres (или другой юзер вместо "postgres" есть в .env.sample)
    - CREATE DATABASE ххх; (название базы данных из .env.sample)
    - \q

7. Примените миграции:
    - python manage.py migrate

8. При регистрации нового пользователя(User) стоит ввести свой "telegram_id" взяв его из бота
   @getmyid_bot (https://t.me/getmyid_bot)

9. Запустите в новом окне терминала Redis:
     - redis-server

10. Запустите в новом окне терминала планировщик задач:
     - celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

11. Запустите сервер:
   - python manage.py runserver

12. Перейдите в бота https://t.me/Useful_habits_corsework_bot, нажмите /start и вуаля!
