import sys
import os
from sqlalchemy.orm import Session

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.infrastructure.database.database import SessionLocal
from src.models.category import Category
from src.models.subcategory import Subcategory
from src.models.transaction import Transaction


def seed_database():
    db: Session = SessionLocal()

    categories = [
        {"name": "Essenciais", "default_percentage": 50, "user_percentage": 50},
        {"name": "Livres", "default_percentage": 30, "user_percentage": 30},
        {"name": "Investimentos", "default_percentage": 20, "user_percentage": 20},
    ]

    subcategories = [
        {"name": "Aluguel", "category": "Essenciais"},
        {"name": "Mercado", "category": "Essenciais"},
        {"name": "Transporte", "category": "Essenciais"},
        {"name": "Lazer", "category": "Livres"},
        {"name": "Eletrônicos", "category": "Livres"},
        {"name": "Reserva de Emergência", "category": "Investimentos"},
        {"name": "Ações", "category": "Investimentos"},
    ]

    # Inserir Categorias
    for cat in categories:
        existing = db.query(Category).filter_by(name=cat["name"]).first()
        if not existing:
            db.add(Category(**cat))

    db.commit()

    # Inserir Subcategorias
    for sub in subcategories:
        category = db.query(Category).filter_by(name=sub["category"]).first()
        if category:
            existing = db.query(Subcategory).filter_by(name=sub["name"]).first()
            if not existing:
                db.add(Subcategory(name=sub["name"], category_id=category.id))

    db.commit()
    db.close()
    print("✅ Banco de dados populado com categorias e subcategorias!")


if __name__ == "__main__":
    seed_database()
