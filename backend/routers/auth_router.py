from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services import AuthService
from postgre import get_session_depends
from DTOs import LoginBody, RegisterBody

auth = APIRouter()

@auth.post("/login")
async def login(
    login_creds: LoginBody,
    postgre_session: AsyncSession = Depends(get_session_depends)
):
    try:
        auth_service: AuthService = await AuthService.create(postgre_session)
        return await auth_service.login(login_creds)
    finally:
        auth_service.close()


@auth.post("/register")
async def register(
    register_creds: RegisterBody,
    postgre_session: AsyncSession = Depends(get_session_depends)
):
    try:
        auth_service: AuthService = await AuthService[AuthService].create(postgre_session)
        return await auth_service.register(register_creds)
    finally:
        auth_service.close()


@auth.post("/logout")
async def logout():
    try:
        auth_service: AuthService = await AuthService[AuthService].create()
        return await auth_service.logout()
    finally:
        auth_service.close()