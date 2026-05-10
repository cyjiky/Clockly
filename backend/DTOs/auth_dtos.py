from pydantic import BaseModel
from datetime import datetime

from app_types import TypeJWT

class LoginBody(BaseModel):
    username: str
    password: str


class RegisterBody(BaseModel):
    username: str
    email: str
    password: str


class AccessResponse(BaseModel):
    access_token: str
    access_token_expiry: datetime

class JWTsResponse(AccessResponse):
    refresh_token: str
    refresh_token_expiry: datetime


class JWTPayload(BaseModel):
    user_id: str
    issued_at: datetime
    expires_at: datetime
    token_type: TypeJWT
