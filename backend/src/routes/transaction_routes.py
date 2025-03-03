from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.src.infrastructure.database.database import get_db
from backend.src.models.transaction import Transaction

router = APIRouter(prefix="/transactions", tags=["Transactions"])


# Endpoint para listas todas transações
@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions
