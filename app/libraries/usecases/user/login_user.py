from fastapi import Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import timedelta
from app.libraries.repositories.user import UserRepository
from app.auth.utils import verify_firebase_token

class LoginUserUsecase:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo = user_repo

    async def exec(self, response, db: Session, token: str): 
        try:
            print(f"トークン:{token}")
            decoded_token = verify_firebase_token(token)
            print(f"decodedトークン:{decoded_token}")
            email = decoded_token.get('email')
            user = await self.user_repo.get_current_user(db, email)
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            response.set_cookie(
                key="auth_token",
                value=token,
                httponly=True,
                secure=True,
                samesite="none",
                max_age=timedelta(days=7)
            )
            
            return {"message": "Successfully logged in"}
        except HTTPException as e:
            print(f"HTTPエラー: {e.detail}")
            raise e
        except Exception as e:
            print(f"一般エラー: {e}")
            raise HTTPException(status_code=400, detail="Login failed")
