from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services import AuthService
from postgre import get_session_depends, merge_model, Users
from DTOs import LoginBody, RegisterBody, JWTsResponse, AccessResponse
from auth.auth_utils import authorize_private_endpoint_via_refresh

from exceptions_handler import endpoint_exception_logger

auth = APIRouter()


@auth.post("/login")
@endpoint_exception_logger
async def login(
    login_creds: LoginBody,
    postgres_session: AsyncSession = Depends(get_session_depends),
) -> JWTsResponse:
    auth_service: AuthService = await AuthService.create(postgres_session)
    try:
        out = await auth_service.login(creds=login_creds)
        await auth_service.close(commit=True)
        return out
    except Exception as e:
        await auth_service.close(commit=False)
        raise e from e


@auth.post("/register")
@endpoint_exception_logger
async def register(
    register_creds: RegisterBody,
    postgres_session: AsyncSession = Depends(get_session_depends),
) -> JWTsResponse:
    auth_service: AuthService = await AuthService.create(postgres_session)
    try:
        out = await auth_service.register(creds=register_creds)
        await auth_service.close(commit=True)
        return out
    except Exception as e:
        await auth_service.close(commit=False)
        raise e from e


@auth.post("/refresh")
@endpoint_exception_logger
async def refresh(
    user_: Users = Depends(authorize_private_endpoint_via_refresh),
    postgres_session: AsyncSession = Depends(get_session_depends),
) -> AccessResponse:
    auth_service: AuthService = await AuthService.create(postgres_session)
    user = await merge_model(user_, postgres_session)
    return await auth_service.refresh(user_id=user.user_id)


# Disabled
# @auth.post("/logout")
# async def logout():
#     try:
#         auth_service: AuthService = await AuthService[AuthService].create()
#         return await auth_service.logout()
#     finally:
#         auth_service.close()
