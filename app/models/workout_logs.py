import datetime
from sqlalchemy import Column, DateTime, BigInteger, String, Integer, ForeignKey, Boolean
from app.settings.database import Base


class WorkOutLogOrm(Base):
  __tablename__ = "workout_logs"

  id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True, index=True)
  exercise_id = Column(Integer, ForeignKey('exercises.id'), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
  weight = Column(Integer, nullable=True)
  rep = Column(Integer, nullable=True)
  set = Column(Integer, nullable=True)
  created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
  updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
