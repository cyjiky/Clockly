from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services import AuthService
from postgre import get_session_depends
from DTOs import LoginBody, RegisterBody, JWTsResponse

auth = APIRouter()


@auth.post("/login")
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
    

# Disabled
# @auth.post("/logout")
# async def logout():
#     try:
#         auth_service: AuthService = await AuthService[AuthService].create()
#         return await auth_service.logout()
#     finally:
#         auth_service.close()
