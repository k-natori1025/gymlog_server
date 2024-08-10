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

class User(BaseModel):
    id: int
    firebase_uid: str
    name: str
    email: Union[str, None] = None
    google_id: Optional[str] = None
    twitter_id: Optional[str] = None
    class Config:
        orm_mode = True

