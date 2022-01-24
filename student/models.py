from django.db import models

# Create your models here.

class Student(models.Model):
    stuid = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=100)