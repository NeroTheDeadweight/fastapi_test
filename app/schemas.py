from pydantic import BaseModel

class OperationRequest(BaseModel):
    operationType: str  # DEPOSIT или WITHDRAW
    amount: float

class WalletResponse(BaseModel):
    id: str
    balance: float