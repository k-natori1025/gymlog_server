import datetime
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, DateTime, BigInteger, String, Boolean
from app.settings.database import Base


class UserOrm(Base):
  __tablename__ = "user"

  id = Column(BigInteger, primary_key=True, nullable=False)
  name = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False)
  created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
  updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
  deleted_at = Column(DateTime, nullable=True)
