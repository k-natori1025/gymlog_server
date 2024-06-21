from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta, datetime, timezone
from app.libraries.repositories.user import UserRepository
from app.auth.utils import verify_firebase_token, create_session_cookie

class LoginUserUsecase:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo = user_repo

    async def exec(self, response, db: Session, token: str): 
        try:
            decoded_token = verify_firebase_token(token)
            expires_in = timedelta(days=5)
            session_cookie = create_session_cookie(token, expires_in)            
            expires = datetime.now(timezone.utc) + expires_in
            email = decoded_token.get('email')
            user = await self.user_repo.get_current_user(db, email)
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            # セッションクッキーをレスポンスに設定
            response.set_cookie(
                key="session",
                value=session_cookie,
                expires=expires,
                httponly=True,
                secure=True,
                samesite="none",
            )
            return {"message": "Successfully logged in"}
        except HTTPException as e:
            print(f"HTTPエラー: {e.detail}")
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except Exception as e:
            print(f"一般エラー: {e}")
            raise HTTPException(status_code=400, detail="Login failed")
