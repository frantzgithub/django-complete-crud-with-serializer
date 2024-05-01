
from rest_framework.views import Request, Response, APIView, status
from .models import Recipes
from ingredients.models import Ingredients
from .serializers import RecipeSerializer

# Create your views here.

class Recipeview(APIView):
    def post(self, req: Request) -> Response:
        serializer = RecipeSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        ingredients = serializer.validated_data.pop("ingredients")
        
        recipe = Recipes.objects.create(**serializer.validated_data)
        
        for ingredient_data in ingredients:
            ingredient = Ingredients.objects.filter(name__iexact=ingredient_data['name'])
            if not ingredient:
                ingredient = Ingredients.objects.create(**ingredient_data)
                recipe.ingredients.add(ingredient)
            else:
                ingredient = ingredient.first()
                recipe.ingredients.add(ingredient)
        serializer = RecipeSerializer(recipe)
        
        return Response(serializer.data, status.HTTP_201_CREATED)
