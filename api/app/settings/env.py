import os
import dotenv
from dotenv import load_dotenv
from pathlib import Path

# TODO: envファイルをappの外に置いても環境変数を取得できるようにする 
# env_path = Path(__file__).parent / '.env'

dotenv.load_dotenv(dotenv.find_dotenv())


def _getenv(key: str):
  env = os.getenv(key)
  if env is None:
        raise ValueError(f"環境変数 {key} が設定されていません。")
  return env


class Env:
  DATABASE_HOST = _getenv("DATABASE_HOST")
  DATABASE_PORT = _getenv("DATABASE_PORT")
  DATABASE_NAME = _getenv("DATABASE_NAME")
  DATABASE_USER = _getenv("DATABASE_USER")
  DATABASE_PASSWORD = _getenv("DATABASE_PASSWORD")
  DATABASE_ROOT_PASSWORD = _getenv("DATABASE_ROOT_PASSWORD")
