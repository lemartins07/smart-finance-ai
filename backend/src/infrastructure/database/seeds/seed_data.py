from sqlalchemy.orm import Session
from src.infrastructure.database.database import SessionLocal
from src.models.user import User
from src.models.institution import Institution
from src.models.bank_account import BankAccount
from src.models.credit_card import CreditCard
from passlib.hash import bcrypt


def seed_database():
    db: Session = SessionLocal()

    # Criar Usuários
    users = [
        {"name": "Leandro Martins", "email": "leandro@email.com", "password": "123456"},
        {"name": "Fabiane Gastring", "email": "fabi@email.com", "password": "senha123"},
    ]

    for user_data in users:
        existing_user = db.query(User).filter_by(email=user_data["email"]).first()
        if not existing_user:
            hashed_password = bcrypt.hash(user_data["password"])
            db.add(
                User(
                    name=user_data["name"],
                    email=user_data["email"],
                    password_hash=hashed_password,
                )
            )

    db.commit()

    # Criar Instituições Financeiras (com número do banco)
    institutions_data = [
        {"name": "Banrisul", "number": 41},
        {"name": "Caixa", "number": 104},
        {"name": "C6 Bank", "number": 336},
        {"name": "Nubank", "number": 260},
    ]

    institution_ids = {}  # Dicionário para armazenar os IDs das instituições

    for inst in institutions_data:
        existing = db.query(Institution).filter_by(name=inst["name"]).first()
        if not existing:
            new_inst = Institution(**inst)
            db.add(new_inst)
            db.commit()
            db.refresh(new_inst)
            institution_ids[inst["name"]] = new_inst.id  # Guarda o ID criado
        else:
            institution_ids[inst["name"]] = existing.id  # Usa o ID existente

    # Criar Contas Bancárias
    bank_accounts = [
        {
            "user_id": 1,
            "name": "Conta Salário",
            "institution_id": institution_ids["Banrisul"],
            "agency": 1234,
            "account_number": 567890,
            "balance": 5000.0,
        },
        {
            "user_id": 1,
            "name": "Conta Poupança",
            "institution_id": institution_ids["Caixa"],
            "agency": 4321,
            "account_number": 123456,
            "balance": 10000.0,
        },
    ]

    for account in bank_accounts:
        existing = (
            db.query(BankAccount)
            .filter_by(account_number=account["account_number"])
            .first()
        )
        if not existing:
            db.add(BankAccount(**account))

    db.commit()

    # Criar Cartões de Crédito
    credit_cards = [
        {
            "user_id": 1,
            "name": "Cartão Nubank",
            "institution_id": institution_ids["C6 Bank"],
            "credit_limit": 5000.0,
            "closing_day": 10,
            "due_day": 20,
        },
        {
            "user_id": 1,
            "name": "Cartão C6",
            "institution_id": institution_ids["Nubank"],
            "credit_limit": 7000.0,
            "closing_day": 5,
            "due_day": 15,
        },
    ]

    for card in credit_cards:
        existing = db.query(CreditCard).filter_by(name=card["name"]).first()
        if not existing:
            db.add(CreditCard(**card))

    db.commit()

    print("✅ Banco de dados populado com sucesso!")


if __name__ == "__main__":
    seed_database()
