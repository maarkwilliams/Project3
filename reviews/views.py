from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Like
from .forms import CommentForm
from recipes.models import Recipe


# View to handle adding a comment to a specific recipe
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            return redirect('recipe_detail', recipe_id=recipe.id)

    else:
        form = CommentForm()
    return render(
        request,
        'comments/add_comment.html',
        {
            'form': form,
            'recipe': recipe
        }
    )


# View to handle liking/unliking a recipe
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    like, created = Like.objects.get_or_create(
        user=request.user,
        recipe=recipe
    )

    if not created:
        like.delete()
    return redirect('recipe_detail', recipe_id=recipe.id)

