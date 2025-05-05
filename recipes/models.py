from django.db import models
from django.conf import settings

CATEGORY_CHOICES = [
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack'),
    ('Drink', 'Drink'),
]

DIFFICULTY_CHOICES = [
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
]

CUISINE_CHOICES = [
    ('American', 'American'),
    ('Italian', 'Italian'),
    ('Chinese', 'Chinese'),
    ('Mexican', 'Mexican'),
    ('Indian', 'Indian'),
]


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    serving_size = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    cuisine = models.CharField(max_length=20, choices=CUISINE_CHOICES)
    image_url = models.URLField(blank=True)
    instructions = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def total_time(self):
        return self.prep_time + self.cook_time


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} of {self.name}"


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_comments'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipe_comment_authors'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.recipe.name}"
