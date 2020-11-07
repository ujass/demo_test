from sqlalchemy.orm import Session

import models, schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


def exist_food(db: Session , food_id : int):
    return db.query(models.Food).filter(models.Food.food_id == food_id).first()
    
def update_food(db: Session , food : schemas.Food,  food_id : int):
    food_available =  db.query(models.Food).filter(models.Food.food_id == food_id).first()
    print(food_available.food_id, food_available.food_name)
    food_available.food_name = food.food_name
    food_available.food_price = food.food_price
    food_available.food_category = food.food_category

    db.commit()
    db.refresh(food_available)
    return food_available

def delete_food(db: Session, food_id : int):
    food_remove = db.query(models.Food).filter(models.Food.food_id == food_id).first()
    db.delete(food_remove)
    db.commit()
    return {"Food removed"}

# def exist_food(db: Session , food_id : int ,  food = food ):
#     food_available =  db.query(models.Food).filter(models.Food.food_id == food_id).first()
    
#     if food_available:
#         food_available = models.Food(food_name = food.food_name )
#         db.add(food_available)
#         db.commit()
#         db.refresh(food_available)
#         return food_available
    









# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()

def get_food_by_category(db: Session , category : str):
    return db.query(models.Food). filter(models.Food.food_category == category).all()

# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


def create_food(db: Session, new_food: schemas.Food ):
    db_food = models.Food(**new_food.dict())
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

def get_food(db: Session):
    return db.query(models.Food).all()

