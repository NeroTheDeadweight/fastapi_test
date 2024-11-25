from fastapi import FastAPI
from app.routes import router as wallet_router
from app.database import engine, Base

# Инициализация приложения FastAPI
app = FastAPI()

# Создание таблиц в базе данных (если они еще не созданы)
Base.metadata.create_all(bind=engine)

# Подключение маршрутов
app.include_router(wallet_router)