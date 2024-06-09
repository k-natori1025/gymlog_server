import datetime
from sqlalchemy import Column, DateTime, BigInteger, String
from app.settings.database import Base


class UserOrm(Base):
  __tablename__ = "users"

  id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
  name = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False)
  password = Column(String(255), nullable=False)
  created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
  updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
  deleted_at = Column(DateTime, nullable=True)
