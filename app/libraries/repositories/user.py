from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import UserOrm
from app.schemas.user import User, UserRegisterRequest, UserRegisterResponse
from app.auth.utils import create_hashed_password

class UserRepository:
    async def create_user(
            self, 
            db: Session, 
            body: UserRegisterRequest
    )->UserRegisterResponse:
        hashed_password = None
        # メールでログインの場合のパスワードをハッシュ化
        if body.password:
            hashed_password = create_hashed_password(body.password)
        user = UserOrm(
            firebase_uid=body.firebase_uid,
            name=body.name, 
            email=body.email, 
            password=hashed_password,
            google_id=body.google_id,
            twitter_id=body.twitter_id
        )
        db.add(user)
        db.commit()
        return UserRegisterResponse.from_orm(user)
    
    async def get_current_user_by_firebase_uid(
            self, 
            db: Session, 
            firebase_uid: str = None
    )->User:
        user_orm = db.scalar(select(UserOrm).where(UserOrm.firebase_uid == firebase_uid))
        if user_orm is None:
            return None
        return User.from_orm(user_orm)
