from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..deps import get_db

router = APIRouter(prefix="/api/products")

@router.get("/")
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@router.post("/")
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
