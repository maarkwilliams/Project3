from django.db import models
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

# Create your models here.
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    prep_time = Column(Integer)
    cook_time = Column(Integer)
    total_time = Column(Integer)
    serving_size = Column(Integer)
    category = Column(String(50))
    difficulty = Column(String(20))
    cuisine = Column(String(50))
    image_url = Column(String(500))
    instructions = Column(Text)
    created_by_id = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<Recipe(name='{self.name}', cuisine='{self.cuisine}')>"
