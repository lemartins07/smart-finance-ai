from sqlalchemy import Column, Integer, String
from src.infrastructure.database.database import Base


class Institution(Base):
    __tablename__ = "institutions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String, nullable=False, unique=True
    )  # Ex: "Nubank", "C6 Bank", "Caixa", etc.
    number = Column(Integer, nullable=False, unique=True)  # número do banco
