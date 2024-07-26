from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel

class UserBase(BaseModel):
    firebase_uid: str
    name: str
    email: Optional[str] = None
    class Config:
        orm_mode = True

class UserRegisterRequest(UserBase):
    email: Optional[str] = None
    password: Optional[str] = None
    google_id: Optional[str] = None
    twitter_id: Optional[str] = None

class UserRegisterResponse(UserBase):
    id: int

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
    firebase_id: int
    name: str
    email: Union[str, None] = None
    google_id: Optional[str] = None
    twitter_id: Optional[str] = None
    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str

