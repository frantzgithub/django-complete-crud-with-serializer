from rest_framework import serializers
from ingredients.serializers import IngredientSerializer

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=1500)
    ingredients = IngredientSerializer(many=True)