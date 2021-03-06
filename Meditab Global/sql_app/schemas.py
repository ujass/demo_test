from typing import List, Optional

from pydantic import BaseModel


class Food(BaseModel):
    food_id : int
    food_name : str
    food_category : str
    food_price : float
    food_quantity : int

    class Config:
        orm_mode = True


class Customer(BaseModel):
    id : int
    name : str

    class Config:
        orm_mode = True

class Order(BaseModel):
    id: int
    food_id: int 
    customer_id : int  
    # status : str


# class ItemBase(BaseModel):
#     title: str  
#     description: Optional[str] = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []

#     class Config:
#         orm_mode = True