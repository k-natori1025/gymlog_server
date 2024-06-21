from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session
import secrets
from passlib.context import CryptContext

from firebase_admin import auth as firebase_auth

from app.models.user import UserOrm
from app.settings.firebase import initialize_firebase

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

initialize_firebase()

def create_hashed_password(password) -> str:
    return pwd_context.hash(password)

# ユーザー認証機能はfirebaseで行うためパスワードの検証は必要なし
# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# ユーザー名既存ユーザーにいるかどうかのチェック
def is_user_exists(db: Session, name: str) -> bool:
    user = db.scalar(select(UserOrm).where(UserOrm.name == name))
    return user is not None

# クライアントから送られてきたfirebaseのid_tokenを検証
def verify_firebase_token(token: str):
    try:
        decoded_token = firebase_auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        print(f"Error verifying Firebase token: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid Firebase token")

# firebaseのid_tokenを用いてセッションクッキーを作成
def create_session_cookie(token: str, expires_in) -> str:
    return firebase_auth.create_session_cookie(token, expires_in=expires_in)

# セッションクッキーの検証
def verify_session_cookie(session_cookie):
    try:
        decoded_token = firebase_auth.verify_session_cookie(session_cookie, check_revoked=True)
        uid = decoded_token["uid"]
        user = firebase_auth.get_user(uid)
        return {"uid": uid, "email": user.email}
    except Exception as e:
        print(f"Error verifying Session Cookie: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid Session Cookie")
