from django.urls import path
from . import views

urlpatterns = [
    path('add_comment/<int:recipe_id>/', views.add_comment, name='add_comment'),
    path('like_recipe/<int:recipe_id>/', views.like_recipe, name='like_recipe'),
]
