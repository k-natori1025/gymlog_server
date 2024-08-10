from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Security, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.settings.database import get_db
from app.libraries.repositories.user import UserRepository
from app.schemas.user import User
from app.auth.utils import verify_firebase_token

security = HTTPBearer()

class GetCurrentUserUseCase:
  def __init__(self, user_repo: UserRepository = Depends()):
      self.user_repo = user_repo
  
  async def exec(
      self, 
      request: Request,
      db: Session = Depends(get_db),
  )->User:
      try:
          auth_header = request.headers.get("Authorization")
          if not auth_header or not auth_header.startswith("Bearer "):
              raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
          token = auth_header.split("Bearer ")[1]

          decoded_token = verify_firebase_token(token)
          firebase_uid = decoded_token.get("uid")
          if not firebase_uid:
              raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
          user = await self.user_repo.get_current_user_by_firebase_uid(db, firebase_uid)
          print(f"@@@現在のuser:{user}@@@")
          if user is None:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
          return user
      except Exception as e:
          print(f"Error in GetCurrentUserUseCase: {str(e)}")
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
