from pydantic import BaseModel, EmailStr


class CreateUserRequestSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class CreateUserResponseSchema(BaseModel):
    access_token: str
    token_type: str