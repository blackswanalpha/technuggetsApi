from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import trainingModel,trainingSchema


def createTraining(url: str, request: trainingSchema.Training, db: Session):
    new_training = trainingModel.Training(name=request.name, desc=request.desc, link=request.link,
                                          location=request.location, provider=request.provider, fee=request.fee,
                                          img=url)

    db.add(new_training)
    db.commit()
    db.refresh(new_training)

    return new_training


def showallTraining(db: Session):
    all_training = db.query(trainingModel.Training).all()
    return all_training


def findById(id, db: Session):
    id_training = db.query(trainingModel.Training).filter(trainingModel.Training.id == id).first()
    if not id_training:
        raise HTTPException(status_code=
                            status.HTTP_404_NOT_FOUND,
                            detail=f"Training with the id: {id} is not available")
        # response.status_code =   status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available"}

    return id_training


def updateTraining(id, request: trainingSchema.UpdateTraining, url: str, db: Session):
    update_training = db.query(trainingModel.Training).filter(trainingModel.Training.id == id)
    request.img = url
    if not update_training.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Training with id {id} not found")

    update_training.update(request.dict())
    # update_training.update(request.dict())
    db.commit()
    return showallTraining(db)


def destroy(id, db: Session):
    delete_training = db.query(trainingModel.Training).filter(trainingModel.Training.id == id).delete(
        synchronize_session=False)

    db.commit()
    return "done deleted"
