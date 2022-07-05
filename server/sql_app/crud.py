from pyexpat import model
from certifi import where
from sqlalchemy.orm import Session
from sqlalchemy import delete
from fastapi import HTTPException

from . import models, schemas



def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    db.delete(user)
    db.commit()

    return "User deleted successfully"



# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(firstName=user.firstName, lastName=user.lastName, DOB=user.DOB, skill=user.skill, available=user.available, )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
