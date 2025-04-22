from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from django.conf import settings

DATABASE_URL = "sqlite:///db.sqlite3"  # or from settings if you prefer

# Create the SQLAlchemy engine and session
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
