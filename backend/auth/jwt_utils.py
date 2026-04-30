import jwt
from DTOs import JWTPayload

from config import settings

def prepare_jwt(jwt_string: str) -> str:
    return jwt_string.removeprefix("Bearer ")


def generate_jwt(payload: JWTPayload) -> str:
    return jwt.encode(
        # Set mode="json" to correctly serialize datetime objects
        payload.model_dump(mode="json"),
        settings.jwt_secret,
        algorithm="HS256",
    )


def extract_jwt_payload(jwt_string: str) -> JWTPayload | None:
    try:
        payload = jwt.decode(
            jwt_string, settings.jwt_secret, algorithms=["HS256"]
        )
        return JWTPayload(**payload)
    except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidKeyError):
        raise Exception("Can't decode jwt")
