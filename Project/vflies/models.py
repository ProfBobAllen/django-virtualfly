from django.db import models

# Create your models here.

class Choices(models.Model):
    teacherID   = models.IntegerField()
    symbol      = models.CharField(max_length=10)
    name        = models.CharField(max_length=20)
    description = models.CharField(max_length=255)

