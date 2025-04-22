from django.shortcuts import render
from .db import SessionLocal

# Create your views here.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()