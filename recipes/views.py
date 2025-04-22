from django.shortcuts import render
from .db import SessionLocal
from django.shortcuts import render

# Create your views here.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def home(request):
    return render(request, 'home.html')