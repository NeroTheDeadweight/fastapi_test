from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Настройки из переменных окружения
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1234@db:5432/wallet_db")

engine = create_engine("postgresql://postgres:1234@localhost:5432/wallet_db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()