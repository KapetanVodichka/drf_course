from rest_framework.pagination import PageNumberPagination


class HabitPagePaginator(PageNumberPagination):
    page_size = 5
