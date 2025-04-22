from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from django.conf import settings

DATABASE_URL = "sqlite:///db.sqlite3"  # or from settings if you prefer

engine = create_engine('sqlite:///db.sqlite3', echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()