import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())


def _getenv(key: str):
  env = os.getenv(key)
  return env


class Env:
  DATABASE_HOST = _getenv("DATABASE_HOST")
  DATABASE_PORT = _getenv("DATABASE_PORT")
  DATABASE_NAME = _getenv("DATABASE_NAME")
  DATABASE_USER = _getenv("DATABASE_USER")
  DATABASE_PASSWORD = _getenv("DATABASE_PASSWORD")
  DATABASE_ROOT_PASSWORD = _getenv("DATABASE_ROOT_PASSWORD")
