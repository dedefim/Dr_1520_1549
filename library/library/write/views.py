from rest_framework import serializers
from .models import TODO, Project
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from rest_framework import mixins

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class TODOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'



class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
class TODOLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class =TODOSerializer
    pagination_class = TODOleLimitOffsetPagination
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
class ProjectLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class =ProjectSerializer
    pagination_class = ProjectleLimitOffsetPagination


class ProjectCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    renderer_classes = [JSORenderer, BrowsableAPIRenderer]

class TODOCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOleSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
