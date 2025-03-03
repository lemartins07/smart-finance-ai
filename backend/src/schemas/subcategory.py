from pydantic import Basemodel
from typing import Optional


class SubcategoryBase(Basemodel):
    name: str
    category_id: int


class SubcategoryCreate(SubcategoryBase):
    pass


class SubcategoryUpdate(Basemodel):
    name: Optional[str] = None
    category_id: Optional[int] = None


class SubcategoryResponse(SubcategoryBase):
    id: int

    class Config:
        orm_mode = True
