from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class BoardSchema(BaseModel):
    id: int
    title: str
    description: str
    public: bool
    archived: bool
    created_by: int
    created_at: datetime
    tasks: list[Any] = Field(default=[], alias="tasks")


class RequestCreateBoardSchema(BaseModel):
    title: str
    description: str
    public: bool


class ResponseCreateBoardSchema(BaseModel):
    id: int
    title: str
    description: str
    public: bool
    archived: bool
    created_by: int
    created_at: datetime


class RequestUpdateBoardSchema(BaseModel):
    title: str
    description: str
    public: bool
    archived: bool


class ResponseAddMemberSchema(BaseModel):
    message: str


class MemberSchema(BaseModel):
    id: int
    username: str
    email: str


class ResponseMoveBoardToArchiveSchema(BaseModel):
    id: int
    title: str
    description: str
    public: bool
    archived: bool
    created_by: int
    created_at: datetime


class ResponseGetBoardStatSchema(BaseModel):
    total: int | None = None
    todo: int | None = None
    in_progress: int | None = None
    done: int | None = None
