from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.infrastructure.database.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )  # 🔹 Usuário dono da transação
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(
        String, nullable=False
    )  # "entrada", "saida", "transferencia"
    bank_account_id = Column(
        Integer, ForeignKey("bank_accounts.id"), nullable=True
    )  # Se pago com conta bancária
    credit_card_id = Column(
        Integer, ForeignKey("credit_cards.id"), nullable=True
    )  # Se pago com cartão
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User")  # Relacionamento com o usuário
    bank_account = relationship("BankAccount")
    credit_card = relationship("CreditCard")
