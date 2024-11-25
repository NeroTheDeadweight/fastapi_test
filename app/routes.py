from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Wallet
from app.schemas import OperationRequest, WalletResponse
import uuid

router = APIRouter()

# Получение сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для операций DEPOSIT и WITHDRAW
@router.post("/api/v1/wallets/{wallet_id}/operation", response_model=WalletResponse)
async def operate_wallet(wallet_id: str, operation: OperationRequest, db: Session = Depends(get_db)):
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()

    if not wallet:
        wallet = Wallet(id=wallet_id, balance=0.0)
        db.add(wallet)

    if operation.operationType == "DEPOSIT":
        wallet.balance += operation.amount
    elif operation.operationType == "WITHDRAW":
        if wallet.balance < operation.amount:
            raise HTTPException(status_code=400, detail="Insufficient funds")
        wallet.balance -= operation.amount
    else:
        raise HTTPException(status_code=400, detail="Invalid operation type")

    db.commit()
    return wallet

# Эндпоинт для получения баланса
@router.get("/api/v1/wallets/{wallet_id}", response_model=WalletResponse)
async def get_wallet_balance(wallet_id: str, db: Session = Depends(get_db)):
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet