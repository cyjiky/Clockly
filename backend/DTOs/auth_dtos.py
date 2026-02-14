from pydantic import BaseModel

import datetime

class LoginBody(BaseModel):
    username: str
    password: str

class RegisterBody(BaseModel):
    username: str
    email: str
    password: str

class JWTsResponse(BaseModel):
    access_token: str
    access_token_expiry: datetime

    refresh_token: str
    refresh_token_expiry: datetime

class JWTPayload(BaseModel):
    user_id: str
    issued_at: datetime
    expires_at: datetime