import datetime
from sqlalchemy import Column, DateTime, BigInteger, String, Integer, ForeignKey, Boolean
from app.settings.database import Base


class UserOrm(Base):
  __tablename__ = "exercises"

  id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True, index=True)
  name = Column(String(255), nullable=False)
  muscle_group_id = Column(Integer, ForeignKey('muscle_groups.id'), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  is_custom = Column(Boolean, nullable=False, default=False)
  created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
  updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
