from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Recipe(models.Model):
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

    name = models.CharField(max_length=255)
    description = models.TextField()
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    total_time = models.IntegerField()
    serving_size = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    cuisine = models.CharField(max_length=20, choices=CUISINE_CHOICES)
    image_url = models.URLField(blank=True)
    instructions = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.total_time = self.prep_time + self.cook_time
        super().save(*args, **kwargs)
