from pydantic import Basemodel
from typing import Optional
from datetime import datetime


class TransactionBase(Basemodel):
    description: str
    amount: float
    subcategory_id: Optional[int] = None


class TransactionCreate(TransactionBase):
    firt_payment_date: datetime


class TransactionUpdate(Basemodel):
    description: Optional[str] = None
    amount: Optional[float] = None
    subcategory_id: Optional[int] = None


class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
