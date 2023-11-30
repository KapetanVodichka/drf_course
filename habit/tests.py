from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import UsefulHabit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='Test@test.com',
            telegram_id=920340035
        )
        self.user.set_password('password')
        self.client.force_authenticate(user=self.user)

    def test_useful_habit(self):
        data = {
            "place": "Кухня",
            "time": "2023-12-01T08:00",
            "action": "выпить воду",
            "time_required": 70,
            "reward": "шоколадка",
        }

        response = self.client.post(
            reverse('habit:create_useful_habits'),
            data,
        )

        if response.status_code != status.HTTP_201_CREATED:
            print(f"Error response content: {response.content.decode('utf-8')}")

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        response = self.client.get(reverse('habit:useful_habits'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        response = self.client.get(f'/habits/useful_habits/{UsefulHabit.objects.all().first().pk}/', follow=True)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        data = {
            'place': 'Водопад'
        }

        response = self.client.patch(
            f'/habits/useful_habits/update/{UsefulHabit.objects.all().first().pk}/',
            data,
            follow=True
        )

        self.assertIn(
            response.status_code,
            [status.HTTP_200_OK, status.HTTP_301_MOVED_PERMANENTLY]
        )

        response = self.client.delete(
            f'/habits/useful_habits/delete/{UsefulHabit.objects.all().first().pk}/',
            data,
            follow=True,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
