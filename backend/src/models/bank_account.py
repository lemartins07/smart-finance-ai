from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.database.database import Base


class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(Integer, primary_key=True, index=True)
    # 🔹 Usuário dono da conta
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # Nome da conta (ex: "Conta Salário")
    name = Column(String, nullable=False)
    # agencia da conta
    agency = Column(Integer, nullable=False)
    # Número da conta
    account_number = Column(Integer, nullable=False)
    # Qual banco pertence
    institution_id = Column(Integer, ForeignKey("institutions.id"), nullable=False)
    # Saldo disponível
    balance = Column(Float, nullable=False, default=0.0)
    primary = Column(
        Integer, nullable=False, default=0
    )  # Define se é a conta principal do usuário

    user = relationship("User")
    institution = relationship("Institution")
