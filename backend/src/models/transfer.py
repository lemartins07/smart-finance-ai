from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.infrastructure.database.database import Base


class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    from_account_id = Column(Integer, ForeignKey("bank_accounts.id"), nullable=False)
    to_account_id = Column(Integer, ForeignKey("bank_accounts.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    from_account = relationship("BankAccount", foreign_keys=[from_account_id])
    to_account = relationship("BankAccount", foreign_keys=[to_account_id])
