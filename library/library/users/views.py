from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.email, User.last_name, User.first_name, User.birthday_year
    serializer_class = UserModelSerializer
