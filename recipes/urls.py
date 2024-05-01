from django.urls import path
from .views import Recipeview

urlpatterns = [
    path("recipes/", Recipeview.as_view(), name="recipes")
]
