from django import forms
from django.forms import modelformset_factory
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    class Meta:
        model = Recipe
        fields = [
            'name', 'description', 'prep_time', 'cook_time',
            'serving_size', 'category', 'difficulty', 'cuisine',
            'instructions'
        ]

IngredientFormSet = modelformset_factory(
    Ingredient,
    fields=['name', 'quantity'],
    extra=1,
)
