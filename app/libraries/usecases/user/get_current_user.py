from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

from app.settings.database import get_db
from app.libraries.repositories.user import UserRepository
from app.auth.utils import verify_session_cookie

security = HTTPBearer()

class GetCurrentUserUseCase:
  def _init_(self, user_repo: UserRepository = Depends()):
      self.user_repo = user_repo
  
  async def exec(self, token: str = Depends(security), db: Session = Depends(get_db)):
      try:
        user_info = verify_session_cookie(token.credentials)
        print(f"@@@@{user_info}@@@@")
        user = await self.user_repo.get_current_user_by_firebase_uid(db, firebase_uid=user_info["firebase_uid"])
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return user

      except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
