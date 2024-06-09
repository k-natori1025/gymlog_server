from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.settings.database import SessionLocal
from app.settings.route import init_route
from app.model import TestUserTable
from app.settings.env import Env

app = FastAPI()
init_route(app)

@app.get("/")
def read_root():
  return {"Hello Word"}



