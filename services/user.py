from fastapi import HTTPException

from models.user import User
from sqlalchemy.orm import Session
from dto import user


def create_user(data: user.User, db):
    db_user = User(firstName=data.firstName, lastName = data.lastName, middleName = data.middleName, position = data.position)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(user_id: int, db):
    return db.query(User).filter(User.id == user_id).first()


def update_user_by_id(user_id: int, data: user.User, db):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.firstName = data.firstName
    db_user.lastName = data.lastName
    db_user.middleName = data.middleName
    db_user.position = data.position
    db.commit()
    return {"message": "User updated successfully"}

def delete_user_by_id(user_id: int, db):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}