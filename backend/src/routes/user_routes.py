from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.src.infrastructure.database.database import get_db
from backend.src.models.user import User
from backend.src.schemas.user import UserCreate, UserResponse
from passlib.hash import bcrypt

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hash(user.password)  # Criptografando a senha
    new_user = User(name=user.name, email=user.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user
