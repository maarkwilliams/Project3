import cloudinary.uploader
from django.shortcuts import render, redirect
from .db import SessionLocal
from django.shortcuts import render
from .models import Recipe

# Create your views here.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def home(request):
    return render(request, 'home.html')

cloudinary.config( 
    cloud_name = "diihryuh9",
    api_key = "488752741654499",
    api_secret = "ExWH3aUo9TcKCrsbYKSx34Mhpnc"
)

def add_recipe(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST['name']
        description = request.POST['description']
        prep_time = int(request.POST['prep_time'])
        cook_time = int(request.POST['cook_time'])
        total_time = prep_time + cook_time
        serving_size = int(request.POST['serving_size'])
        category = request.POST['category']
        difficulty = request.POST['difficulty']
        cuisine = request.POST['cuisine']
        image = request.FILES['image']
        instructions = request.POST['instructions']

        # Upload to Cloudinary
        upload_result = cloudinary.uploader.upload(image)
        image_url = upload_result['secure_url']

        # Save the new recipe in the database
        db = SessionLocal()
        new_recipe = Recipe(
            name=name,
            description=description,
            prep_time=prep_time,
            cook_time=cook_time,
            total_time=total_time,
            serving_size=serving_size,
            category=category,
            difficulty=difficulty,
            cuisine=cuisine,
            image_url=image_url,
            instructions=instructions,
            created_by_id=request.user.id
        )
        db.add(new_recipe)
        db.commit()
        db.close()

        return redirect('home')

    return render(request, 'add_recipe.html')