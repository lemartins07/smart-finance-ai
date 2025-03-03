from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str  # Senha em texto puro (será criptografada)


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
