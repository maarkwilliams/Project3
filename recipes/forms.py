from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Recipe
        fields = [
            'name', 'description', 'prep_time', 'cook_time',
            'serving_size', 'category', 'difficulty', 'cuisine',
            'instructions'
        ]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['name'].required = False
            self.fields['quantity'].required = False
            self.fields['id'] = forms.CharField(required=False, widget=forms.HiddenInput())

IngredientFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    extra=1,
    can_delete=True,
    validate_min=False
)
