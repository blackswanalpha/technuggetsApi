from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List

import schema
from . import jobModel


def createJob(url:str,request: schema.Job, db: Session):
    new_job = jobModel.Job(name=request.name, desc = request.desc, link = request.link, venue = request.venue, provider= request.provider, requirement = request.requirement, img = url)

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


def showallJob(db:Session):
    all_job = db.query(jobModel.Job).all()
    return all_job


def findById(id, db: Session ):
    id_job = db.query(jobModel.Job).filter(jobModel.Job.id == id).first()
    if not id_job:
        raise HTTPException(status_code=
                            status.HTTP_404_NOT_FOUND,
                            detail=f"Job with the id: {id} is not available")
        # response.status_code =   status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available"}

    return id_job


def updateJob(id, request: schema.UpdateJob, url:str, db: Session ):
    update_job = db.query(jobModel.Job).filter(jobModel.Job.id == id)
    request.img =url
    if not update_job.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} not found")



    update_job.update( request.dict())
    # update_job.update(request.dict())
    db.commit()
    return showallJob(db)


def destroy( id, db: Session):
    delete_job = db.query(jobModel.Job).filter(jobModel.Job.id == id).delete(synchronize_session=False)

    db.commit()
    return "done deleted"


