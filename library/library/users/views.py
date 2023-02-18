from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer
from rest_framework import serializers
from rest_framework import mixins

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users
        fields = '__all__'

class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
class USerLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =UserSerializer
    pagination_class = UserleLimitOffsetPagination

class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]