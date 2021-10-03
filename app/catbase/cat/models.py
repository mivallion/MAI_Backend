from django.conf import settings
from django.db import models


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


class CatReview(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    review_id = models.ForeignKey(Review, to_field='id', on_delete=models.CASCADE)
    cat_id = models.ForeignKey(Cat, to_field='id', on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
