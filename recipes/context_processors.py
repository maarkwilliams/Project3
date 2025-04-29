from .models import Recipe

def recipe_categories(request):
    """Add category and cuisine choices to all templates."""
    category_field = Recipe._meta.get_field('category')
    cuisine_field = Recipe._meta.get_field('cuisine')

    category_choices = [choice[0] for choice in category_field.choices]
    cuisine_choices = [choice[0] for choice in cuisine_field.choices]

    return {
        'category_choices': category_choices,
        'cuisine_choices': cuisine_choices,
    }
