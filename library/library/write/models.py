
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=128)
    link = models.CharField(max_length=256)
    workers = models.CharField(max_length=512)

    def __str__(self):
        return self.title


class TODO(models.Model):
    text = models.TextField()
    Project = models.OneToOneField(Project, on_delete=models.CASCADE)
    data = models.DateTimeField()
    data_update = models.DateTimeField()


