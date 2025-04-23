import cloudinary.uploader
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm, IngredientFormSet, IngredientForm
from .models import Recipe, Ingredient
from django.contrib.auth.decorators import login_required
from django import forms
from reviews.forms import CommentForm
from reviews.models import Like
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

# Cloudinary config
cloudinary.config(
    cloud_name="diihryuh9",
    api_key="488752741654499",
    api_secret="ExWH3aUo9TcKCrsbYKSx34Mhpnc"
)

@login_required
def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        formset = IngredientFormSet(request.POST, prefix='ingredient_set')
        
        logger.info(f"POST data: {request.POST}")
        logger.info(f"Formset prefix: {formset.prefix}")
        logger.info(f"Formset is valid: {formset.is_valid()}")
        if not formset.is_valid():
            logger.error(f"Formset errors: {formset.errors}")
            logger.error(f"Formset non-form errors: {formset.non_form_errors()}")

        if recipe_form.is_valid() and formset.is_valid():
            image = recipe_form.cleaned_data['image']
            upload_result = cloudinary.uploader.upload(image)
            image_url = upload_result['secure_url']

            recipe = recipe_form.save(commit=False)
            recipe.image_url = image_url
            recipe.created_by = request.user
            recipe.save()
            
            logger.info(f"Recipe created with ID: {recipe.id}")

            logger.info(f"Number of forms in formset: {len(formset)}")
            for i, form in enumerate(formset):
                logger.info(f"Form {i} data: {form.cleaned_data}")
                if form.cleaned_data.get('name') or form.cleaned_data.get('quantity'):
                    ingredient = form.save(commit=False)
                    ingredient.recipe = recipe
                    ingredient.save()
                    logger.info(f"Ingredient saved: {ingredient.name} - {ingredient.quantity}")
                else:
                    logger.info(f"Form {i} is empty, skipping")

            return redirect('recipe_list')
    else:
        recipe_form = RecipeForm()
        formset = IngredientFormSet(queryset=Ingredient.objects.none(), prefix='ingredient_set')
        logger.info(f"Initial formset prefix: {formset.prefix}")

    return render(request, 'recipes/add_recipe.html', {
        'recipe_form': recipe_form,
        'formset': formset,
    })

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    likes_count = Like.objects.filter(recipe=recipe).count()
    comment_form = CommentForm()

    if request.method == 'POST':
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
    recipe = get_object_or_404(Recipe, id=recipe_id, created_by=request.user)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        ingredient_forms = IngredientFormSet(request.POST, instance=recipe, prefix='ingredient_set')
        
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            
            if 'image' in request.FILES:
                try:
                    upload_result = cloudinary.uploader.upload(request.FILES['image'])
                    recipe.image_url = upload_result['secure_url']
                except Exception as e:
                    messages.error(request, 'Failed to upload new image.')
                    logger.exception('Cloudinary upload failed during edit.')
                    return render(request, 'recipes/edit_recipe.html', {
                        'form': form,
                        'ingredient_forms': ingredient_forms,
                        'recipe': recipe
                    })

            recipe.save()
            
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
        form = RecipeForm(instance=recipe)
        ingredient_forms = IngredientFormSet(instance=recipe, prefix='ingredient_set')
    
    return render(request, 'recipes/edit_recipe.html', {
        'form': form,
        'ingredient_forms': ingredient_forms,
        'recipe': recipe
    })

