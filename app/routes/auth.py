from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, security
from ..deps import get_db, get_current_user

router = APIRouter(prefix="/api/auth")

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = security.hash_password(user.password)
    db_user = models.User(name=user.name, email=user.email, password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    token = security.create_token({"user_id": db_user.id})

    return {"token": token, "user": db_user}

@router.post("/login")
def login(data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or not security.verify_password(data.password, user.password):
        return {"error": "Invalid credentials"}

    token = security.create_token({"user_id": user.id})

    return {"token": token, "user": user}

@router.get("/me")
def me(user=Depends(get_current_user)):
    return user
