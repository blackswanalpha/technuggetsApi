from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List

import schema
from . import eventModel


def createEvent(url:str,request: schema.Event, db: Session):
    new_event = eventModel.Event(name=request.name, desc = request.desc, link = request.link, venue = request.venue, speaker = request.speaker, price = request.price, img = url)

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event


def showallEvent(db:Session):
    all_event = db.query(eventModel.Event).all()
    return all_event


def findById(id, db: Session ):
    id_event = db.query(eventModel.Event).filter(eventModel.Event.id == id).first()
    if not id_event:
        raise HTTPException(status_code=
                            status.HTTP_404_NOT_FOUND,
                            detail=f"Event with the id: {id} is not available")
        # response.status_code =   status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available"}

    return id_event


def updateEvent(id, request: schema.UpdateEvent, url:str, db: Session ):
    update_event = db.query(eventModel.Event).filter(eventModel.Event.id == id)
    request.img =url
    if not update_event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")



    update_event.update( request.dict())
    # update_event.update(request.dict())
    db.commit()
    return showallEvent(db)


def destroy( id, db: Session):
    delete_event = db.query(eventModel.Event).filter(eventModel.Event.id == id).delete(synchronize_session=False)

    db.commit()
    return "done deleted"


