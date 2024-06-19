from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True

class UserRegisterRequest(UserBase):
    password: str

class UserRegisterResponse(UserBase):
    pass

class UserUpdate(UserBase):
    name: Optional[str] = None
    email: Optional[str] = None

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

class TokenForm(BaseModel):
    token: str

class TokenData(BaseModel):
    name: Union[str, None] = None

class User(BaseModel):
    id: int
    name: str
    email: Union[str, None] = None
    disabled: Union[bool, None] = None
    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str

