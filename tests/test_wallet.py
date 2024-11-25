import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_wallet_operations():
    async with AsyncClient(app=app, base_url="http://test") as client:
        wallet_id = "test-wallet"

        # Депозит
        response = await client.post(f"/api/v1/wallets/{wallet_id}/operation", json={
            "operationType": "DEPOSIT",
            "amount": 1000
        })
        assert response.status_code == 200
        assert response.json()["balance"] == 1000

        # Снятие
        response = await client.post(f"/api/v1/wallets/{wallet_id}/operation", json={
            "operationType": "WITHDRAW",
            "amount": 500
        })
        assert response.status_code == 200
        assert response.json()["balance"] == 500

        # Проверка баланса
        response = await client.get(f"/api/v1/wallets/{wallet_id}")
        assert response.status_code == 200
        assert response.json()["balance"] == 500
        # Тест на снятие больше, чем доступно на балансе
        response = await client.post(f"/api/v1/wallets/{wallet_id}/operation", json={
            "operationType": "WITHDRAW", "amount": 1000})
        assert response.status_code == 400  # Ошибка, недостаточно средств
        assert response.json()['detail'] == "Insufficient funds"