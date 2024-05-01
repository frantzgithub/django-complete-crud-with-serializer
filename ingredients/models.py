from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ManyToManyField("recipes.Recipes", related_name="ingredients")
    
    def __repr__(self) -> str:
        return f"<[{self.id}] {self.name}>"
