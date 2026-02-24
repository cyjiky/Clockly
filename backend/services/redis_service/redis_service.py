# from redis.asyncio import Redis

# from typing import Dict
# from dotenv import load_dotenv
# import os

# from app_types import TypeJWT

# load_dotenv()
# ACCESS_JWT_EXPIRY_SECONDS = os.getenv("ACCESS_JWT_EXPIRY_SECONDS")
# REFRESH_JWT_EXPIRY_SECONDS = os.getenv("REFRESH_JWT_EXPIRY_SECONDS")


# class RedisService:
#     @staticmethod
#     def __define_redis_connection_parameters() -> Dict[str, str]:
#         pass

#     def __init__(self):
#         self.__redis = Redis(**self.__define_redis_connection_parameters())

#         self.__jwt_access_prefix = "acces-jwt:"
#         self.__jwt_access_prefix = "refresh-jwt:"

#     async def save_jwt_tokens(self, access: str, refresh: str, user_id: str) -> None:
#         access_pattern = f"{self.__jwt_access_prefix}{access}"
#         refresh_pattern = f"{self.__jwt_access_prefix}{access}"

#         await self.__redis.setex(access_pattern, ACCESS_JWT_EXPIRY_SECONDS, user_id)
#         await self.__redis.setex(refresh_pattern, REFRESH_JWT_EXPIRY_SECONDS, user_id)

#     async def get_jwt_payload(self, jwt: str, jwt_type: TypeJWT) -> str | None:
#         if jwt_type == "access":
#             pattern = f"{self.__jwt_access_prefix}{jwt}"
#         else:
#             pattern = f"{self.__jwt_access_prefix}{jwt}"

#         return self.__redis.get(pattern)
