from django.contrib.auth.models import User
from rest_framework import serializers

from cat.models import Cat
from reviews.models import Review


class ReviewSerializer(serializers.Serializer):

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance

    user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all(),
                                              read_only=False, allow_null=False)
    cat = serializers.PrimaryKeyRelatedField(many=False, queryset=Cat.objects.all(),
                                             read_only=False, allow_null=False)

    class Meta:
        model = Review
        fields = ['id', 'review_title', 'review_text', 'general_rating', 'attractiveness', 'sociability',
                  'playfulness', 'user', 'cat']
