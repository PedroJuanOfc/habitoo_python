from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr = Field(..., description="E-mail do usuário")
    password: str = Field(..., min_length=1, description="Senha em texto puro")


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserPublic(BaseModel):
    id: str
    email: EmailStr
    name: str


class AuthResponse(BaseModel):
    token: Token
    user: UserPublic
