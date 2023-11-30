from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from habit.models import UsefulHabit, PleasantHabit, Habit
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer, UsefulHabitSerializer, PublicHabitsSerializer, PleasantHabitSerializer, \
    CreatePleasantHabitSerializer, UpdateUsefulHabitSerializer
from habit.paginators import HabitPagePaginator


class PublishedHabitListAPIView(ListAPIView):
    serializer_class = PublicHabitsSerializer
    queryset = Habit.objects.filter(is_public=True)
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    pagination_class = HabitPagePaginator


class UsefulHabitListAPIView(ListAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    pagination_class = HabitPagePaginator

    def get_queryset(self):
        user = self.request.user
        return UsefulHabit.objects.filter(user=user)


class UsefulHabitCreateAPIView(CreateAPIView):
    serializer_class = UsefulHabitSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class UsefulHabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = UsefulHabit.objects.all()
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny, IsOwner]


class UsefulHabitUpdateAPIView(UpdateAPIView):
    serializer_class = UpdateUsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]
    permission_classes = [AllowAny, IsOwner]


class UsefulHabitDestroyAPIView(DestroyAPIView):
    queryset = UsefulHabit.objects.all()
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny, IsOwner]


class PleasantHabitListAPIView(ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    pagination_class = HabitPagePaginator
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny, IsOwner]

    def get_queryset(self):
        return PleasantHabit.objects.filter(user=self.request.user)


class PleasantHabitCreateAPIView(CreateAPIView):
    serializer_class = CreatePleasantHabitSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class PleasantHabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PleasantHabitUpdateAPIView(UpdateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PleasantHabitDestroyAPIView(DestroyAPIView):
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
