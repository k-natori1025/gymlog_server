from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.settings.database import SessionLocal
from app.model import TestUserTable
from app.settings.env import Env

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/")
def read_root():
  return {"Hello Word"}

#　テストユーザー情報一覧取得
@app.get("/test_users")
def get_user_list(db: Session = Depends(get_db)):
    users = db.query(TestUserTable).all()
    return users


