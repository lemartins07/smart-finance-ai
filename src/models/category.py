from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from infrastructure.database.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    default_percentage = Column(Float, nullable=False)
    user_percentage = Column(Float, nullable=False)

    subcategories = relationship("Subcategory", back_populates="category")
