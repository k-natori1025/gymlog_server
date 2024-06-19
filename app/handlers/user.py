from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.schemas.user import UserRegisterRequest, TokenForm
from app.libraries.usecases.user.login_user import LoginUserUsecase
from app.libraries.repositories.user import UserRepository
from app.settings.database import get_db
from app.auth.utils import is_user_exists

router = APIRouter()
security = HTTPBearer()

@router.post("/user/", tags=["ユーザー"], summary="ユーザーを登録する")
async def create_user(
    body: UserRegisterRequest,
    db: Session = Depends(get_db),
    user_repo: UserRepository = Depends()
):
    try:
        if is_user_exists(db, body.name):
            raise HTTPException(status_code=400, detail="Username already taken")
        response = await user_repo.create(db, body)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login",tags=["ユーザー"], summary="ログイン")
async def login_user(
    response: Response,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
    login_user_usecase: LoginUserUsecase = Depends()
):
    print(f"credentials: {credentials.credentials}")
    response = await login_user_usecase.exec(response, db, token=credentials.credentials)
    return response
