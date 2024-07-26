import datetime
from sqlalchemy import Column, DateTime, BigInteger, String
from app.settings.database import Base


class UserOrm(Base):
  __tablename__ = "users"

  id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True, index=True)
  firebase_uid = Column(String(255), unique=True, nullable=False, index=True)
  name = Column(String(255), unique=True, nullable=False)
  email = Column(String(255), unique=True, nullable=True)
  password = Column(String(255), nullable=True)
  google_id = Column(String(100), unique=True, nullable=True)
  twitter_id = Column(String(100), unique=True, nullable=True)
  created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
  updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
  deleted_at = Column(DateTime, nullable=True)
