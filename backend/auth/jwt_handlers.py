import jwt
from DTOs import JWTPayload

import os
from dotenv import load_dotenv

load_dotenv()


def prepare_jwt(jwt_string: str) -> str:
    return jwt_string.removeprefix("Bearer")


def generate_jwt(payload: JWTPayload) -> str:
    return jwt.encode(
        payload.model_dump(), os.getenv("JWT_SECRET_KEY"), algorithm="HS256"
    )


def extract_jwt_payload(jwt_string: str) -> JWTPayload | None:
    try:
        payload = jwt.decode(
            jwt_string, os.getenv("JWT_SECRET_KEY"), algorithms=["HS256"]
        )
        return JWTPayload(**payload)
    except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidKeyError):
        raise Exception("Can't decode jwt")
