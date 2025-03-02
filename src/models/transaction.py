from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from infrastructure.database.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)  # Valor da parcela
    total_amount = Column(Float, nullable=False)  # Valor total da compra
    installments = Column(
        Integer, nullable=False, default=1
    )  # Número total de parcelas
    installment_number = Column(
        Integer, nullable=False, default=1
    )  # Número da parcela atual
    subcategory_id = Column(Integer, ForeignKey("subcategories.id"), nullable=False)
    first_payment_date = Column(DateTime, nullable=False)  # Data da primeira cobrança
    created_at = Column(DateTime, server_default=func.now())


subcategory = relationship("Subcategory", back_populates="transactions")
