from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List

import schema
from . import roleModel


def createRole(request: schema.Role, db: Session):
    new_role = roleModel.Role(name=request.name)

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return new_role


def showallRole(db:Session):
    all_role = db.query(roleModel.Role).all()
    return all_role


def findById(id, db: Session ):
    id_role = db.query(roleModel.Role).filter(roleModel.Role.id == id).first()
    if not id_role:
        raise HTTPException(status_code=
                            status.HTTP_404_NOT_FOUND,
                            detail=f"Role with the id: {id} is not available")
        # response.status_code =   status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available"}

    return id_role


def updateRole(id, request: schema.Role, db: Session ):
    update_role = db.query(roleModel.Role).filter(roleModel.Role.id == id)

    if not update_role.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {id} not found")

    update_role.update( request.dict())
    db.commit()
    return "update_role"


def destroy( id, db: Session):
    delete_role = db.query(roleModel.Role).filter(roleModel.Role.id == id).delete(synchronize_session=False)

    db.commit()
    return "done deleted"


