from pydantic import BaseModel
from typing import List, Optional

class Training(BaseModel):
    name :str
    desc:str
    link:str
    location:str
    provider: str
    fee: int

class UpdateTraining(BaseModel):
    name: str
    desc: str
    link: str
    location: str
    provider: str
    fee: int
    img : str



class ShowTraining(BaseModel):
    name: str
    desc: str
    link: str
    location: str
    provider: str
    fee: int
    img : str


    class Config():
        orm_mode=True