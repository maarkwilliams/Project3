import cloudinary.uploader
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm, IngredientFormSet, IngredientForm
from .models import Recipe, Ingredient
from django.contrib.auth.decorators import login_required
from django import forms
from reviews.forms import CommentForm
from reviews.models import Like
from django.contrib import messages
from django.forms import inlineformset_factory

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
        formset = IngredientFormSet(request.POST)

        if recipe_form.is_valid() and formset.is_valid():
            image = recipe_form.cleaned_data['image']
            upload_result = cloudinary.uploader.upload(image)
            image_url = upload_result['secure_url']

            recipe = recipe_form.save(commit=False)
            recipe.image_url = image_url
            recipe.created_by = request.user
            recipe.save()

            for form in formset:
                ingredient = form.save(commit=False)
                ingredient.recipe = recipe
                ingredient.save()

            return redirect('recipe_list')
    else:
        recipe_form = RecipeForm()
        formset = IngredientFormSet(queryset=Ingredient.objects.none())

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
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.user != recipe.created_by and not request.user.is_staff:
        return redirect('recipe_detail', recipe_id=recipe.id)

    IngredientFormSet = inlineformset_factory(
        Recipe, Ingredient, form=IngredientForm, extra=1, can_delete=True
    )

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        formset = IngredientFormSet(request.POST, instance=recipe)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
        formset = IngredientFormSet(instance=recipe)

    return render(
        request,
        'recipes/edit_recipe.html',
        {
            'form': form,
            'ingredient_forms': formset,
            'recipe': recipe
        }
    )