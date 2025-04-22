import cloudinary.uploader
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.decorators import login_required

# Cloudinary config
cloudinary.config( 
    cloud_name="diihryuh9",
    api_key="488752741654499",
    api_secret="ExWH3aUo9TcKCrsbYKSx34Mhpnc"
)

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            
            upload_result = cloudinary.uploader.upload(image)
            image_url = upload_result['secure_url']
            
            new_recipe = form.save(commit=False)
            new_recipe.image_url = image_url
            new_recipe.created_by = request.user
            new_recipe.save()

            return redirect('recipe_list')
    else:
        form = RecipeForm()

    return render(request, 'recipes/add_recipe.html', {'form': form})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
