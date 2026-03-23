from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, EmailStr

class UserRole(StrEnum):
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'



class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    avatar_url: str | None = None
    created_at: datetime


class RequestUpdateUserSchema(BaseModel):
    username: str
    email: EmailStr
    role: UserRole
    avatar_url: str

class RequestUpdateUserPasswordSchema(BaseModel):
    new_password: str

class RequestUpdateUserAvatarSchema(BaseModel):
    avatar_url: str