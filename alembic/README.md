 FastAPI Wallet Application

Это приложение на FastAPI для управления кошельками с возможностью выполнения операций DEPOSIT и WITHDRAW. Приложение подключается к базе данных PostgreSQL, поддерживает миграции через Alembic и может быть запущено в Docker-контейнерах с помощью Docker Compose.

## Стек технологий

- **Backend**: FastAPI
- **База данных**: PostgreSQL
- **Миграции**: Alembic
- **Тестирование**: pytest, pytest-asyncio
- **Асинхронные запросы**: httpx (для тестов)
- **Контейнеризация**: Docker, Docker Compose

## Установка и запуск

1. **Клонируйте репозиторий**:
   ```bash
   git clone <ссылка на репозиторий>
   cd <папка с проектом>

    Создайте и активируйте виртуальное окружение:

python -m venv .venv
source .venv/bin/activate  # Для Linux/Mac
.venv\Scripts\activate     # Для Windows

Установите зависимости:

pip install -r requirements.txt

Запустите Docker контейнеры: Для запуска приложения и базы данных в Docker контейнерах, используйте docker-compose:

    docker-compose up --build

    Запустите приложение: Приложение будет доступно по адресу http://localhost:8000.

Эндпоинты API
1. POST /api/v1/wallets/{WALLET_UUID}/operation

Выполняет операцию с кошельком (DEPOSIT или WITHDRAW).

Тело запроса:

{
  "operationType": "DEPOSIT",  # Или "WITHDRAW"
  "amount": 1000
}

Ответ:

    200 OK при успешной операции.
    400 Bad Request при ошибке (например, недостаточно средств).

2. GET /api/v1/wallets/{WALLET_UUID}

Получает текущий баланс кошелька.

Ответ:

{
  "wallet_id": "12345",
  "balance": 1000
}

Миграции базы данных

Миграции базы данных выполняются с помощью Alembic. Чтобы применить миграции, выполните:

docker-compose exec app alembic upgrade head

Тестирование

Для тестирования приложения используется pytest и pytest-asyncio.

    Запуск тестов: Для запуска тестов выполните:

    pytest

    Тестирование асинхронных функций: В тестах используется httpx.AsyncClient для выполнения асинхронных HTTP-запросов к вашему приложению.


Примечания

    Асинхронные запросы: В тестах используются асинхронные запросы с помощью httpx.AsyncClient, так как FastAPI поддерживает асинхронность.
    Конфигурация Docker: Все настройки для работы с базой данных и приложением заданы в docker-compose.yml. Это позволяет без проблем запустить приложение в контейнерах.


