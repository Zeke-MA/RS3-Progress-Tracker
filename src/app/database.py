from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.app.config import settings


Base = declarative_base

SessionLocal = None

def create_db_connection():
    engine = create_engine(settings.DATABASE_URL)

