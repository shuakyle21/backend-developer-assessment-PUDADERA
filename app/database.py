import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Overridable so the DB file can live on a mounted volume (e.g. /app/data/data.db)
# without shadowing the app code copied into the image at /app.
DATABASE_PATH = os.getenv("DATABASE_PATH", "./data.db")

engine = create_engine(f"sqlite:///{DATABASE_PATH}", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()