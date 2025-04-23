from .models import Recipe

def recipe_categories(request):
    """Add category and cuisine choices to all templates."""
    category_choices = [choice[0] for choice in Recipe._meta.get_field('category').choices]
    cuisine_choices = [choice[0] for choice in Recipe._meta.get_field('cuisine').choices]
    
    return {
        'category_choices': category_choices,
        'cuisine_choices': cuisine_choices,
    } 