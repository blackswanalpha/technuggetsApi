from pydantic import BaseModel
from typing import List, Optional


class Login(BaseModel):
    name: str
    password: str


class ShowLogin(BaseModel):
    name: str
    password: str

    class Config():
        orm_mode = True


class Role(BaseModel):
    name: str

class ShowRole(BaseModel):

    name:str

    class Config():
        orm_mode = True


class Event (BaseModel):
    name :str
    desc:str
    link:str
    venue:str
    speaker :str
    price:int

class UpdateEvent(BaseModel):
    name: str
    desc: str
    link: str
    venue: str
    speaker: str
    price: int
    img : str



class ShowEvent(BaseModel):
    name: str
    desc: str
    link: str
    venue: str
    speaker: str
    price: int
    img : str


    class Config():
        orm_mode=True



class Job(BaseModel):
    name :str
    desc:str
    link:str
    venue:str
    provider: str
    requirement: str

class UpdateJob(BaseModel):
    name: str
    desc: str
    link: str
    venue: str
    provider: str
    requirement: str
    img : str



class ShowJob(BaseModel):
    name: str
    desc: str
    link: str
    venue: str
    provider: str
    requirement: str
    img : str


    class Config():
        orm_mode=True

