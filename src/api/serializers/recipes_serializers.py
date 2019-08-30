from rest_framework import serializers

from api.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ('id', 'user',)
