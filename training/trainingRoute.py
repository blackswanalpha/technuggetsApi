import shutil

from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from typing import List
import database
from . import trainingSchema
from sqlalchemy.orm import Session
from . import trainingRepo
from database import engine, get_db
import uuid

IMAGEDIR = "media/"

router = APIRouter(
    prefix="/training",
    tags=['training']
)

get_db = database.get_db


@router.post('/createTraining', response_model=trainingSchema.ShowTraining, status_code=status.HTTP_201_CREATED)
async def create_training(request: trainingSchema.Training = Depends(), file: UploadFile = File(...), db: Session = Depends(get_db)):
    # with open("media/" + file.filename, "wb") as image:
    #
    #     shutil.copyfileobj(file.file, image)

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    url = str("media/" + file.filename)

    return trainingRepo.createTraining(url, request, db)


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

@router.get('/showAllTraining', response_model=List[trainingSchema.ShowTraining])
def show(db: Session = Depends(get_db)):
    return trainingRepo.showallTraining(db)


@router.get('/findByTrainingId/{id}', response_model=trainingSchema.ShowTraining)
def show_by_id(id, db: Session = Depends(get_db)):
    return trainingRepo.findById(id, db)


@router.put('/updateTraining/{id}', status_code=status.HTTP_202_ACCEPTED)
async  def update(id, request: trainingSchema.UpdateTraining = Depends(), file: UploadFile = File(...), db: Session = Depends(get_db)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    url = str("media/" + file.filename)
    return trainingRepo.updateTraining(id, request,url, db)


@router.delete("/deleteTraining/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return trainingRepo.destroy(id, db)
