from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
]
