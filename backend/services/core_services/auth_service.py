from fastapi import HTTPException

import json
from uuid import uuid4
from datetime import datetime, timedelta
from dotenv import load_dotenv
from os import getenv

from DTOs import LoginBody, RegisterBody, JWTPayload, JWTsResponse
from auth import *
from services import CoreServiceBase
from utils import validate_email, validate_password
from postgre import Users, Calendars

load_dotenv()

ACCESS_JWT_EXPIRY_SECONDS = int(getenv("ACCESS_JWT_EXPIRY_SECONDS"))
REFRESH_JWT_EXPIRY_SECONDS = int(getenv("REFRESH_JWT_EXPIRY_SECONDS"))

DATETIME_FORMAT = getenv("DATETIME_FORMAT")


class AuthService(CoreServiceBase):
    def _generate_auth_tokens(self, new_user_id: str):
        access_jwt_expiry = datetime.now() + timedelta(
            seconds=ACCESS_JWT_EXPIRY_SECONDS
        )
        access_jwt_payload = JWTPayload(
            user_id=new_user_id,
            issued_at=datetime.now(),
            expires_at=access_jwt_expiry,
        )

        refresh_jwt_expiry = datetime.now() + timedelta(
            seconds=REFRESH_JWT_EXPIRY_SECONDS
        )
        refresh_jwt_payload = JWTPayload(
            user_id=new_user_id,
            issued_at=datetime.now(),
            expires_at=refresh_jwt_expiry,
        )

        access_jwt = generate_jwt(access_jwt_payload)
        refresh_jwt = generate_jwt(refresh_jwt_payload)

        return JWTsResponse(
            access_token=access_jwt,
            access_token_expiry=access_jwt_expiry,
            refresh_token=refresh_jwt,
            refresh_token_expiry=refresh_jwt_expiry,
        )

    async def authorize_request_jwt_and_return_user(self, jwt: str) -> Users:
        """Raise 401 on failed authorization"""
        
        prepared_jwt = prepare_jwt(jwt_string=jwt)
        jwt_payload = extract_jwt_payload(jwt_string=prepared_jwt)

        user = await self._PostgreService.get_user_by_id(user_id=jwt_payload.user_id)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized"
            )

        return user

    async def login(self, creds: LoginBody) -> JWTsResponse:
        potential_user = await self._PostgreService.get_user_by_username(
            username=creds.username
        )

        if not validate_password(creds.password):
            raise HTTPException(
                status_code=400,
                detail="Password isn't secure enough."
                "At least one uppercase letter and number!",
            )
        if not potential_user:
            raise HTTPException(
                status_code=400,
                detail="Such user doesn't exist, try to register first.",
            )

        return self._generate_auth_tokens(new_user_id=potential_user.user_id)

    async def register(self, creds: RegisterBody) -> JWTsResponse:
        if not validate_email(creds.email):
            raise HTTPException(
                status_code=400, detail="Invalid email provided"
            )
        if not validate_password(creds.password):
            raise HTTPException(
                status_code=400,
                detail="Password isn't secure enough"
                "At least one uppercase letter and number!",
            )

        if await self._PostgreService.get_user_by_username(
            username=creds.username
        ):
            # code 409 - collision, such instance already exists
            raise HTTPException(
                status_code=409, detail="This username is already used"
            )
        if await self._PostgreService.get_user_by_email(email=creds.email):
            raise HTTPException(
                status_code=409, detail="This email is already used"
            )

        password_hash = hash_password(creds.password)
        new_user_id = str(uuid4())
        new_user = Users(
            user_id=new_user_id,
            username=creds.username,
            email=creds.email,
            password_hash=password_hash,
        )

        initial_calendar_id = str(uuid4())
        initial_calendar = Calendars(
            calendar_id=initial_calendar_id,
            name=creds.username,
            color="#4361EE",
            is_initial=True,
            user_id=new_user_id,
        )

        await self._PostgreService.flush_models(new_user, initial_calendar)

        return self._generate_auth_tokens(new_user_id=new_user_id)

    async def logout(self):
        raise Exception("Method is disabled")

    async def change_username(self):
        pass

    async def change_password(self):
        pass
