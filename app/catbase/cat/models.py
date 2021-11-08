from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Cat(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    birth_year = models.PositiveIntegerField()
    description = models.CharField(max_length=4000, null=True)


class Review(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    review_title = models.CharField(max_length=50)
    review_text = models.CharField(max_length=4000, null=True)
    general_rating = models.PositiveIntegerField()
    attractiveness = models.PositiveIntegerField()
    sociability = models.PositiveIntegerField()
    playfulness = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
