from django.contrib.auth.models import User
from django.db import models

from cat.models import Cat


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    review_title = models.CharField(max_length=50)
    review_text = models.CharField(max_length=4000, null=True)
    general_rating = models.PositiveIntegerField()
    attractiveness = models.PositiveIntegerField()
    sociability = models.PositiveIntegerField()
    playfulness = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
