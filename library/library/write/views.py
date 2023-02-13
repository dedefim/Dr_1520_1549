from rest_framework import serializers
from .models import TODO, Project
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class TODOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'




