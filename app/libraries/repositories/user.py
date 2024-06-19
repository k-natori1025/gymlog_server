from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import UserOrm
from app.schemas.user import User, UserRegisterRequest, UserRegisterResponse
from app.auth.utils import create_hashed_password

class UserRepository:
    async def create(self, db: Session, body: UserRegisterRequest)->UserRegisterResponse:
        # パスワードをハッシュ化
        hashed_password = create_hashed_password(body.password)
        user = UserOrm(name=body.name, email=body.email, password=hashed_password)
        db.add(user)
        db.commit()
        return UserRegisterResponse.from_orm(user)
    
    async def get_current_user(self, db: Session, email: str)->User:
        user_orm = db.scalar(select(UserOrm).where(UserOrm.email == email))
        if user_orm is None:
            return None
        return User.from_orm(user_orm)
