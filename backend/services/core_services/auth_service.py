from fastapi import HTTPException

from uuid import uuid4
import datetime
from dotenv import load_dotenv
from os import getenv

from DTOs import LoginBody, RegisterBody, JWTPayload, JWTsResponse
from auth import hash_password, generate_jwt
from services import CoreServiceBase
from utils import validate_email, validate_password
from postgre import User

load_dotenv()

ACCESS_JWT_EXPIRY_SECONDS = int(getenv("ACCESS_JWT_EXPIRY_SECONDS"))
REFRESH_JWT_EXPIRY_SECONDS = int(getenv("REFRESH_JWT_EXPIRY_SECONDS"))

class AuthService(CoreServiceBase):
    async def login(self, creds: LoginBody) -> JWTsResponse:
        pass

    async def register(self, credentials: RegisterBody) -> JWTsResponse:
        if not validate_email(credentials.email):
            raise HTTPException(
                status_code=400,
                detail="Invalid email provided"
            )
        if not validate_password(credentials.password):
            raise HTTPException(
                status_code=400,
                detail="Password isn't secure enough."
                "At least one uppercase letter and number!"
            )

        if await self._PostgreService.get_user_by_username(username=credentials.username):
            # code 409 - collision, such instance already exists
            raise HTTPException(
                status_code=409,
                detail="User with this email already exist."
            )
        if await self._PostgreService.get_user_by_email(email=credentials.email):
            raise HTTPException(
                status_code=409,
                detail="This email is already used."
            )

        password_hash = hash_password(credentials.password)

        new_user_id = uuid4()
        new_user = User(
            user_id=uuid4(),
            username=credentials.username,
            email=credentials.email,
            password_hash=password_hash
        )

        await self._PostgreService.flush_models(new_user)

        # TODO: Take this logic to another function for reusing purposes
        access_jwt_expiry = datetime.now() + datetime.timedelta(
            seconds=ACCESS_JWT_EXPIRY_SECONDS
        )
        access_jwt_payload = JWTPayload(
            user_id=new_user_id,
            issued_at=datetime.now(),
            expires_at=access_jwt_expiry
        )

        refresh_jwt_expiry = datetime.now() + datetime.timedelta(
            seconds=REFRESH_JWT_EXPIRY_SECONDS
        )
        refresh_jwt_payload = JWTPayload(
            user_id=new_user_id,
            issued_at=datetime.now(),
            expires_at=refresh_jwt_expiry
        )

        access_jwt = generate_jwt(access_jwt_payload)
        refresh_jwt = generate_jwt(refresh_jwt_payload)

        return JWTsResponse(
            access_token=access_jwt,
            access_token_expiry=access_jwt_expiry,
            refresh_token=refresh_jwt,
            refresh_jwt_expiry=refresh_jwt_expiry
        )

    async def logout(self):
        raise Exception(
            "Not implemented yet! This method would work,"
            "if the application could store tokens and deactive them."
        )
    
    async def change_username(self):
        pass

    async def change_password(self):
        pass