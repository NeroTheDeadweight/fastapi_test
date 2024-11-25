from sqlalchemy import Column, String, Float
from app.database import Base

class Wallet(Base):
    __tablename__ = "wallets"
    id = Column(String, primary_key=True, index=True)
    balance = Column(Float, default=0.0)