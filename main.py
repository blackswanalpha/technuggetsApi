from database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List

from event import eventRoute
from job import jobRoute
from login import loginRoute
from role import roleRoute
from training import trainingRoute

app = FastAPI()



origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(loginRoute.router)
app.include_router(roleRoute.router)
app.include_router(eventRoute.router)
app.include_router(jobRoute.router)
app.include_router(trainingRoute.router)