import cloudinary.uploader
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm, IngredientFormSet
from .models import Recipe, Ingredient
from django.contrib.auth.decorators import login_required
from reviews.forms import CommentForm
from reviews.models import Like
from django.contrib import messages
from django.http import HttpResponseForbidden

# Cloudinary configuration for image uploads
cloudinary.config(
    cloud_name="diihryuh9",
    api_key="488752741654499",
    api_secret="ExWH3aUo9TcKCrsbYKSx34Mhpnc"
)

@login_required
def add_recipe(request):
    # Handles both GET and POST requests for adding a new recipe
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        formset = IngredientFormSet(request.POST, prefix='ingredient_set')

        if recipe_form.is_valid() and formset.is_valid():
            # Upload the image to Cloudinary and get the secure URL
            image = recipe_form.cleaned_data['image']
            upload_result = cloudinary.uploader.upload(image)
            image_url = upload_result['secure_url']

            # Save the recipe instance without committing to assign extra fields
            recipe = recipe_form.save(commit=False)
            recipe.image_url = image_url
            recipe.created_by = request.user
            recipe.save()

            # Save each valid ingredient form and associate it with the recipe
            for form in formset:
                name = form.cleaned_data.get('name')
                quantity = form.cleaned_data.get('quantity')

                if name or quantity:
                    ingredient = form.save(commit=False)
                    ingredient.recipe = recipe
                    ingredient.save()

            # Redirect to recipe list after successful submission
            return redirect('recipe_list')
    else:
        # Initialize empty forms for GET request
        recipe_form = RecipeForm()
        formset = IngredientFormSet(
            queryset=Ingredient.objects.none(),
            prefix='ingredient_set'
        )

    return render(request, 'recipes/add_recipe.html', {
        'recipe_form': recipe_form,
        'formset': formset,
    })

def recipe_list(request):
    # View to list all recipes
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
    })

def recipe_detail(request, recipe_id):
    # View for a specific recipe's details
    recipe = get_object_or_404(Recipe, id=recipe_id)
    likes_count = Like.objects.filter(recipe=recipe).count()
    comment_form = CommentForm()

    if request.method == 'POST':
        # Handle like functionality for authenticated users
        if request.user.is_authenticated:
            if not Like.objects.filter(user=request.user, recipe=recipe).exists():
                Like.objects.create(user=request.user, recipe=recipe)
            return redirect('recipe_detail', recipe_id=recipe.id)

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'likes_count': likes_count,
        'form': comment_form,
    })

@login_required
def delete_recipe(request, recipe_id):
    # Allow only recipe creators or staff to delete a recipe
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.user == recipe.created_by or request.user.is_staff:
        recipe.delete()
        messages.success(request, "Recipe deleted successfully.")
        return redirect('recipe_list')
    else:
        messages.error(request, "You are not authorized to delete this recipe.")
        return redirect('recipe_detail', recipe_id=recipe.id)

@login_required
def edit_recipe(request, recipe_id):
    # View for editing an existing recipe
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if recipe.created_by != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to edit this recipe.")

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        ingredient_forms = IngredientFormSet(
            request.POST, instance=recipe, prefix='ingredient_set')

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user

            # Handle image upload if a new image is provided
            if 'image' in request.FILES:
                try:
                    upload_result = cloudinary.uploader.upload(request.FILES['image'])
                    recipe.image_url = upload_result['secure_url']
                except Exception as e:
                    messages.error(request, 'Failed to upload new image.')
                    return render(request, 'recipes/edit_recipe.html', {
                        'form': form,
                        'ingredient_forms': ingredient_forms,
                        'recipe': recipe
                    })

            recipe.save()

            # Handle saving or deleting ingredients
            if ingredient_forms.is_valid():
                for form in ingredient_forms:
                    if form.cleaned_data.get('DELETE'):
                        form.instance.delete()
                    elif form.cleaned_data.get('name') or form.cleaned_data.get('quantity'):
                        ingredient = form.save(commit=False)
                        ingredient.recipe = recipe
                        ingredient.save()

                messages.success(request, 'Recipe updated successfully!')
                return redirect('recipe_detail', recipe_id=recipe.id)
            else:
                messages.error(request, 'Please correct the errors in the ingredient forms.')
        else:
            messages.error(request, 'Please correct the errors in the recipe form.')
    else:
        # Prepopulate forms with existing recipe data
        form = RecipeForm(instance=recipe)
        ingredient_forms = IngredientFormSet(instance=recipe, prefix='ingredient_set')

    return render(request, 'recipes/edit_recipe.html', {
        'form': form,
        'ingredient_forms': ingredient_forms,
        'recipe': recipe
    })

def recipes_by_category(request, category):
    # Filter recipes based on category
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'filter_title': f"{category} Recipes"
    })

def recipes_by_cuisine(request, cuisine):
    # Filter recipes based on cuisine
    recipes = Recipe.objects.filter(cuisine=cuisine)
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'filter_title': f"{cuisine} Cuisine"
    })
