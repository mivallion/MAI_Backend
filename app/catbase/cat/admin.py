from django.contrib import admin

from .models import Cat, CatReview, Review

admin.site.register(Cat)
admin.site.register(Review)
admin.site.register(CatReview)
