import os
import dotenv
from pathlib import Path

dotenv.load_dotenv(dotenv.find_dotenv())


def _getenv(key: str):
  env = os.getenv(key)
  if env is None:
        raise ValueError(f"環境変数 {key} が設定されていません。")
  return env


class Env:
  # データベース関連
  DATABASE_HOST = _getenv("DATABASE_HOST")
  DATABASE_PORT = _getenv("DATABASE_PORT")
  DATABASE_NAME = _getenv("DATABASE_NAME")
  DATABASE_USER = _getenv("DATABASE_USER")
  DATABASE_PASSWORD = _getenv("DATABASE_PASSWORD")
  DATABASE_ROOT_PASSWORD = _getenv("DATABASE_ROOT_PASSWORD")

  # firebase関連
  FIREBASE_DICT = {
     "type": _getenv("FIREBASE_TYPE"),
     "project_id": _getenv("FIREBASE_PROJECT_ID"),
     "private_key_id": _getenv("FIREBASE_PRIVATE_KEY_ID"),
     "private_key": _getenv("FIREBASE_PRIVATE_KEY"),
     "client_email": _getenv("FIREBASE_CLIENT_EMAIL"),
     "client_id": _getenv("FIREBASE_CLIENT_ID"),
     "auth_uri": _getenv("FIREBASE_AUTH_URI"),
     "token_uri": _getenv("FIREBASE_TOKEN_URI"),
     "auth_provider_x509_cert_url": ("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
     "client_x509_cert_url": _getenv("FIREBASE_CLIENT_X509_CERT_URL"),
     "universe_domain": _getenv("FIREBASE_UNIVERSE_DOMAIN"), 
  }

