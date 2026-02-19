from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models
from ..deps import get_db, get_current_user

router = APIRouter(prefix="/api/orders")

@router.get("/")
def list_orders(user=Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.user_id == user.id).all()

@router.post("/")
def create_order(data: dict, user=Depends(get_current_user), db: Session = Depends(get_db)):
    order = models.Order(user_id=user.id, total=data["total"])
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
