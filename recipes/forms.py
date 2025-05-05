from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient, Comment


# Form for creating or editing a recipe
class RecipeForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Recipe
        fields = [
            'name', 'description', 'prep_time', 'cook_time',
            'serving_size', 'category', 'difficulty', 'cuisine',
            'instructions'
        ]


# Form for creating or editing an ingredient associated with a recipe
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['name'].required = False
            self.fields['quantity'].required = False
            self.fields['id'] = forms.CharField(
                required=False,
                widget=forms.HiddenInput()
            )

# Create a formset for handling multiple ingredients for a recipe
IngredientFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    extra=1,
    can_delete=True,
    validate_min=False
)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("Comment cannot be blank or contain only whitespace.")
        return content