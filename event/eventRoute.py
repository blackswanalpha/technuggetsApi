import shutil

from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from typing import List
import database, schema
from sqlalchemy.orm import Session
from . import eventRepo
from database import engine, get_db
import uuid

IMAGEDIR = "media/"

router = APIRouter(
    prefix="/event",
    tags=['event']
)

get_db = database.get_db


@router.post('/createEvent', response_model=schema.ShowEvent, status_code=status.HTTP_201_CREATED)
async def create_event(request: schema.Event = Depends(), file: UploadFile = File(...), db: Session = Depends(get_db)):
    # with open("media/" + file.filename, "wb") as image:
    #
    #     shutil.copyfileobj(file.file, image)

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    url = str("media/" + file.filename)

    return eventRepo.createEvent(url, request, db)


# @router.put("/images/{id}")
# async def create_upload_file( title:str,file: UploadFile = File(...)):
# 
#     file.filename = f"{uuid.uuid4()}.jpg"
#     contents = await file.read()  # <-- Important!
# 
#     # example of how you can save the file
#     with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
#         f.write(contents)
# 
#     return {"filename": file.filename, "request": title}

@router.get('/showAllEvent', response_model=List[schema.ShowEvent])
def show(db: Session = Depends(get_db)):
    return eventRepo.showallEvent(db)


@router.get('/findByEventId/{id}', response_model=schema.ShowEvent)
def show_by_id(id, db: Session = Depends(get_db)):
    return eventRepo.findById(id, db)


@router.put('/updateEvent/{id}', status_code=status.HTTP_202_ACCEPTED)
async  def update(id, request: schema.UpdateEvent = Depends(), file: UploadFile = File(...), db: Session = Depends(get_db)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    url = str("media/" + file.filename)
    return eventRepo.updateEvent(id, request,url, db)


@router.delete("/deleteEvent/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return eventRepo.destroy(id, db)
