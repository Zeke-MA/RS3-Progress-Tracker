from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeMeta, Session
from sqlalchemy import Engine
from config import settings



Base: DeclarativeMeta = declarative_base()

DATABASE_URL = settings.DATABASE_URL

if not DATABASE_URL:
    raise Exception("DATABASE_URL is not set in .env file")

DB_ENGINE = create_engine(settings.DATABASE_URL)

    
DB_SES_MAKER = sessionmaker(autoflush=False,bind=DB_ENGINE)

def init_db():
    try:
        import models
        Base.metadata.create_all(bind=DB_ENGINE)
    except Exception as e:
        print(e)