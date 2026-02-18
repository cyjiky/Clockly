from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services import AuthService
from postgre import get_session_depends
from DTOs import LoginBody, RegisterBody, JWTsResponse

auth = APIRouter()

@auth.post("/login")
async def login(
    login_creds: LoginBody,
    postgre_session: AsyncSession = Depends(get_session_depends)
) -> JWTsResponse:
    exception_occured = False
    try:
        auth_service: AuthService = await AuthService.create(postgre_session)
        return await auth_service.register(login_creds)
    except Exception as e:
        exception_occured = True
        raise e from e
    finally:
        if not exception_occured:
            await auth_service.close(commit=True)


@auth.post("/register")
async def register(
    register_creds: RegisterBody,
    postgre_session: AsyncSession = Depends(get_session_depends)
) -> JWTsResponse:
    exception_occured = False

    try:
        auth_service: AuthService = await AuthService.create(postgre_session)
        return await auth_service.register(register_creds)
    except Exception as e:
        exception_occured = True
        raise e from e
    finally:
        if not exception_occured:
            await auth_service.close(commit=True)


@auth.post("/logout")
async def logout():
    try:
        auth_service: AuthService = await AuthService[AuthService].create()
        return await auth_service.logout()
    finally:
        auth_service.close()