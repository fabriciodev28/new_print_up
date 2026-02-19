from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
