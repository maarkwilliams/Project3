from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'prep_time', 'cook_time', 'serving_size', 'category', 'difficulty', 'cuisine', 'image', 'instructions']
    
    image = forms.ImageField(required=True)

    def clean_total_time(self):
        prep_time = self.cleaned_data.get('prep_time')
        cook_time = self.cleaned_data.get('cook_time')
        return prep_time + cook_time
