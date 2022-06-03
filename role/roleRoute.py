from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
import database, schema
from sqlalchemy.orm import Session
from . import roleRepo
from database import engine, get_db

router = APIRouter(
    prefix="/role",
    tags=['role']
)

get_db = database.get_db


@router.post('/createRole', response_model=schema.ShowRole, status_code=status.HTTP_201_CREATED)
def create_role(request: schema.Role, db: Session = Depends(get_db)):
    return roleRepo.createRole(request, db)


@router.get('/showAllRole', response_model=List[schema.ShowRole])
def show(db: Session = Depends(get_db)):
    return roleRepo.showallRole(db)


@router.get('/findByRoleId/{id}', response_model=schema.ShowRole)
def show_by_id(id, db: Session = Depends(get_db)):
    return roleRepo.findById(id, db)


@router.put('/updateRole/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schema.Role, db: Session = Depends(get_db)):
    return roleRepo.updateRole(id, request, db)


@router.delete("/deleteRole/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return roleRepo.destroy(id, db)
