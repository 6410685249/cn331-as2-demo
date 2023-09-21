from django.db import models
from ..subjects.models import Subject

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    id = models.IntegerField()
    status = models.CharField(max_length=20)
    subjects = models.ManyToManyField(Subject, blank=True, related_name="list Subjects")
