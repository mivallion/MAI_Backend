from django.http import JsonResponse, Http404
from django.views import View
from rest_framework import viewsets

from cat.models import Cat
from cat.serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
