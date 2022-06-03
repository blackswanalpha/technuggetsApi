from fastapi import APIRouter
import database, schema

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from . import loginRepo

router = APIRouter(
    prefix="/login",
    tags=['login']
)

get_db = database.get_db


@router.post('/', response_model=schema.ShowLogin)
def create_user(request: schema.Login, db: Session = Depends(get_db)):
    return loginRepo.create(request, db)


@router.get('/{id}', response_model=schema.ShowLogin)
def get_user(id: int, db: Session = Depends(get_db)):
    return loginRepo.show(id, db)