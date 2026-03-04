from pydantic import BaseModel, EmailStr

class LoginResponseSchema(BaseModel):
    access_token: str
    token_type: str

class LoginRequestSchema(BaseModel):
    email: EmailStr
    password: str
