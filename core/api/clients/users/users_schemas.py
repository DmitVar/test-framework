from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, EmailStr

class UserRole(StrEnum):
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'

class TaskPriority(StrEnum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

class TaskStatus(StrEnum):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


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
    avatar_url: str | None = None

class RequestUpdateUserPasswordSchema(BaseModel):
    new_password: str

class RequestUpdateUserAvatarSchema(BaseModel):
    avatar_url: str

class UserTaskSchema(BaseModel):
    title: str
    description: str
    priority: TaskPriority
    parent_task_id: int | None = None
    created_by: int
    created_at: datetime
    id: int
    status: TaskStatus
    order: int
    board_id: int
    assignee_id: int | None = None
    updated_at: datetime | None = None

class ResponseGetUserAvatarSchema(BaseModel):
    user_id: int
    avatar_url: str | None = None