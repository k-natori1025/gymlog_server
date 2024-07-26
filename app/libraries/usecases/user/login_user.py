from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta, datetime, timezone
from app.libraries.repositories.user import UserRepository
from app.auth.utils import verify_firebase_token, create_session_cookie, get_user_info_from_token
from app.schemas.user import UserRegisterRequest
from app.settings.env import Env

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
            google_id = decoded_token.get('firebase', {}).get('identities', {}).get('google.com', [None])[0]
            twitter_id = decoded_token.get('firebase', {}).get('identities', {}).get('twitter.com', [None])[0]
            
            user_info = get_user_info_from_token(decoded_token)

            login_type = self._get_login_type(user_info)
            
            user = await self.user_repo.get_current_user(
                db, 
                email=user_info['email'], 
                google_id=user_info['google_id'], 
                twitter_id=user_info['twitter_id']
            )

            if user is None:
                if login_type == 'email':
                    # For email login, if user doesn't exist, raise an error
                    raise HTTPException(status_code=404, detail="User not found. Please register first.")
                else:
                    # For social login, create a new user if not exists
                    user_data = UserRegisterRequest(
                        name=user_info['name'],
                        email=user_info['email'],
                        google_id=user_info['google_id'],
                        twitter_id=user_info['twitter_id']
                    )
                    user = await self.user_repo.create_user(db, user_data)

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
        
    def _get_login_type(self, user_info: dict) -> str:
        if user_info['google_id']:
            return 'google'
        elif user_info['twitter_id']:
            return 'twitter'
        else:
            return 'email'
