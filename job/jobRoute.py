import shutil

from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from typing import List
import database, schema
from sqlalchemy.orm import Session
from . import jobRepo
from database import engine, get_db
import uuid

IMAGEDIR = "media/"

router = APIRouter(
    prefix="/job",
    tags=['job']
)

get_db = database.get_db


@router.post('/createJob', response_model=schema.ShowJob, status_code=status.HTTP_201_CREATED)
async def create_job(request: schema.Job = Depends(), file: UploadFile = File(...), db: Session = Depends(get_db)):
    # with open("media/" + file.filename, "wb") as image:
    #
    #     shutil.copyfileobj(file.file, image)

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    url = str("media/" + file.filename)

    return jobRepo.createJob(url, request, db)


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

@router.get('/showAllJob', response_model=List[schema.ShowJob])
def show(db: Session = Depends(get_db)):
    return jobRepo.showallJob(db)


@router.get('/findByJobId/{id}', response_model=schema.ShowJob)
def show_by_id(id, db: Session = Depends(get_db)):
    return jobRepo.findById(id, db)


@router.put('/updateJob/{id}', status_code=status.HTTP_202_ACCEPTED)
async  def update(id, request: schema.UpdateJob = Depends(), file: UploadFile = File(...), db: Session = Depends(get_db)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    url = str("media/" + file.filename)
    return jobRepo.updateJob(id, request,url, db)


@router.delete("/deleteJob/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return jobRepo.destroy(id, db)
