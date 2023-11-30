from rest_framework.generics import CreateAPIView

from users.serializers import UserRegistrationSerializer


class RegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.set_password(new_user.password)
        new_user.save()
