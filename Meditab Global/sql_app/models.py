from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Food(Base):
    __tablename__ = "foods"

    food_id = Column(Integer, primary_key = True, index = True)
    food_name = Column(String, unique = True , index = True)
    food_category  = Column(String)
    food_price = Column(Float)
    food_quantity = Column(Integer)

    orders = relationship("Order", backref= "food")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key = True , index = True)
    name = Column(String, index = True)

    orders = relationship("Order", backref="customer")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key = True,  index = True)
    food_id = Column(Integer , ForeignKey("foods.food_id"))
    customer_id = Column(Integer , ForeignKey("customers.id"))
    # status = Column(String, default = "Order Placed")

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")