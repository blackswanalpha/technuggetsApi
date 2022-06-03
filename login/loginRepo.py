from sqlalchemy.orm import Session
from . import loginModel
import  schema
from fastapi import HTTPException, status
from .hashing import Hash


def create(request: schema.Login, db: Session):
    new_user = loginModel.User(
        name=request.name,status = 1, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user = db.query(loginModel.User).filter(loginModel.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user