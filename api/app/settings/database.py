from app.settings.env import Env
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

_database_url = URL.create(
  drivername="mysql+mysqldb",
  username=Env.DATABASE_USER,
  password=Env.DATABASE_PASSWORD,
  host=Env.DATABASE_HOST,
  port=Env.DATABASE_PORT,
  database=Env.DATABASE_NAME
)

Engine = create_engine(_database_url, encoding="utf-8", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Base = declarative_base()

