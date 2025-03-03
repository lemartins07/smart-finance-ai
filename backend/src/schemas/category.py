from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    name: str
    default_percentage: float
    user_percentage: float = Field(default=0.0)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    default_percentage: Optional[float] = None


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True
