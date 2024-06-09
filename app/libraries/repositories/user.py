from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.user import UserOrm
from app.schemas.user import UserRegisterRequest, UserRegisterResponse
from app.auth.utils import get_password_hash

class UserRepository:
    async def create(self, db: Session, body: UserRegisterRequest)->UserRegisterResponse:
        # パスワードをハッシュ化
        hashed_password = get_password_hash(body.password)
        user = UserOrm(name=body.name, email=body.email, password=hashed_password)
        db.add(user)
        db.commit()
        return UserRegisterResponse.from_orm(user)
