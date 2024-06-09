from fastapi import Depends
from sqlalchemy.orm import Session

from app.libraries.repositories.user import UserRepository
from app.schemas.user import UserRegisterRequest

class CreateUserUsecase:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo = user_repo

    async def exec(self, db: Session, body: UserRegisterRequest):
        return await self.user_repo.create(db, body)
