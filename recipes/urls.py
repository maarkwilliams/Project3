from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),
    path('category/<str:category>/', views.recipes_by_category, name='recipes_by_category'),
    path('cuisine/<str:cuisine>/', views.recipes_by_cuisine, name='recipes_by_cuisine'),
]
