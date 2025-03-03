from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.src.infrastructure.database.database import get_db
from backend.src.models.subcategory import Subcategory

router = APIRouter(prefix="/subcategories", tags=["Subcategories"])


# Endpoint para listar todas as Sub categorias
@router.get("/")
def get_subcategories(db: Session = Depends(get_db)):
    subcategories = db.query(Subcategory).all()
    return subcategories
