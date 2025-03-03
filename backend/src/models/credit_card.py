from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.database.database import Base


class CreditCard(Base):
    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )  # 🔹 Usuário dono do cartão
    # Nome do cartão (ex: "Cartão Nubank")
    name = Column(String, nullable=False)
    # Banco do cartão
    institution_id = Column(
        Integer, ForeignKey("institutions.id"), nullable=False
    )  # Limite do cartão

    credit_limit = Column(Float, nullable=False)
    # Dia do fechamento da fatura
    closing_day = Column(Integer, nullable=False)
    due_day = Column(Integer, nullable=False)  # Dia de vencimento da fatura

    user = relationship("User")  # Relacionamento com o usuário
    institution = relationship("Institution")  # Relacionamento com o banco
