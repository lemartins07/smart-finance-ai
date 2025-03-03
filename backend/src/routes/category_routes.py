from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.src.infrastructure.database.database import get_db
from backend.src.models.category import Category

router = APIRouter(prefix="/categories", tags=["Categories"])


# Endpoint para listar todas as categorias
@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories
