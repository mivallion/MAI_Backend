from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    birth_year = models.PositiveIntegerField()
    description = models.CharField(max_length=4000, null=True)
