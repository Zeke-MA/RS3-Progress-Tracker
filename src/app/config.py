import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(dotenv_path=BASE_DIR / ".env")

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    print(DATABASE_URL)

settings = Settings()
