from django.urls import path

from habit.apps import HabitConfig
from habit.views import UsefulHabitListAPIView, UsefulHabitCreateAPIView, UsefulHabitRetrieveAPIView, \
    UsefulHabitUpdateAPIView, UsefulHabitDestroyAPIView, PleasantHabitListAPIView, PleasantHabitCreateAPIView, \
    PleasantHabitRetrieveAPIView, PleasantHabitUpdateAPIView, PleasantHabitDestroyAPIView, PublishedHabitListAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('useful_habits', UsefulHabitListAPIView.as_view(), name='useful_habits'),
    path('useful_habits/create/', UsefulHabitCreateAPIView.as_view(), name='create_useful_habits'),
    path('useful_habits/<int:pk>/', UsefulHabitRetrieveAPIView.as_view(), name='overview_useful_habits'),
    path('useful_habits/update/<int:pk>/', UsefulHabitUpdateAPIView.as_view(), name='update_useful_habits'),
    path('useful_habits/delete/<int:pk>/', UsefulHabitDestroyAPIView.as_view(), name='delete_useful_habits'),

    path('pleasant_habits', PleasantHabitListAPIView.as_view(), name='pleasant_habits'),
    path('pleasant_habits/create/', PleasantHabitCreateAPIView.as_view(), name='create_pleasant_habit'),
    path('pleasant_habits/<int:pk>/', PleasantHabitRetrieveAPIView.as_view(), name='overview_pleasant_habit'),
    path('pleasant_habits/update/<int:pk>/', PleasantHabitUpdateAPIView.as_view(), name='update_pleasant_habit'),
    path('pleasant_habits/delete/<int:pk>/', PleasantHabitDestroyAPIView.as_view(), name='delete_pleasant_habit'),

    path('public_habits', PublishedHabitListAPIView.as_view(), name='public_habits')
]
