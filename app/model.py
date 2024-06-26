from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.settings.database import Base, Engine

# テーブル定義
class TestUserTable(Base):
  __tablename__ = 'test_user'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(30), nullable=False)
  email = Column(String(128), nullable=False)

# モデル定義
class TestUser(BaseModel):
  id: int
  name: str
  email: str

def main():
  # テーブル構築
  Base.metadata.create_all(bind=Engine)

if __name__ == '__main__':
  main()
