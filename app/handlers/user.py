from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.user import UserRegisterRequest
from app.libraries.usecases.user.create_user import CreateUserUsecase
from app.libraries.repositories.user import UserRepository
from app.settings.database import SessionLocal, get_db
from app.auth.utils import is_user_exists

router = APIRouter()

@router.post("/user/", tags=["ユーザー"], summary="ユーザーを登録する")
async def create_user(
    body: UserRegisterRequest,
    db: Session = Depends(get_db),
    user_repo: UserRepository = Depends()
):
    try:
        if is_user_exists(db, body.name):
            raise HTTPException(status_code=400, detail="Username already registered")
        response = await user_repo.create(db, body)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.post("/token")
# async def login_for_access_token(
#     form_data: OAuth2PasswordRequestForm = Depends(),
# ) -> Token:
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return Token(access_token=access_token, token_type="bearer")


# @router.get("/users/me/", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user


# @router.get("/users/me/items/")
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     return [{"item_id": "Foo", "owner": current_user.username}]

