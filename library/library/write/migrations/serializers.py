from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer



class Project:
    def __init__(self, title, link):
        self.title = title
        self.link = link
    def __str__(self):
        return self.title
class Text:
    def __init__(self, text):
        self.text = text
class Article:
    def __init__(self, title, workers):
        self.title = title
        self.workers = workers
class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    link = serializers.CharField(max_length=256)
    workers = serializers.CharField(max_length=512)

    def create(self, validated_data):
        return Project(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year',
                                                instance.birthday_year)
        return instance


class TODO(serializers.ModelSerializer):

    Project = ProjectSerializer()
    class Meta:
        data = serializers.DateTimeField()
        data_update = serializers.DateTimeField()
title = ('Заметки', "Иванов")
serializer = ProjectSerializer(title)
print(serializer.data)
print(type(serializer.data))
renderer = JSONRenderer()
json_bytes = renderer.render(serializer.data)
print(json_bytes)
print(type(json_bytes))
stream = io.BytesIO(json_bytes)
data = JSONParser().parse(stream)
print(data)
print(type(data))
serializer = ProjectSerializer(data=data)
print(serializer.is_valid())
print(serializer.validated_data)
print(type(serializer.validated_data))
data = {'title': 'Project1', 'link': "https://gdcdn.mrgcdn.ru/"}
serializer = ProjectSerializer(data=data)
serializer.is_valid()
author = serializer.save()
data = {'title': 'project2', 'link': "https://gdcdn"}
serializer = ProjectSerializer(author, data=data)
serializer.is_valid()
author = serializer.save()
data = {'workers': "Иванов"}
serializer = ProjectSerializer(author, data=data, partial=True)
serializer.is_valid()
author = serializer.save()

