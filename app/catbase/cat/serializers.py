from rest_framework import serializers

from cat.models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'birth_year', 'name', 'description']
