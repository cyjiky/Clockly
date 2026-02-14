from fastapi import APIRouter

from services import AuthService

auth = APIRouter()

@auth.post("/login")
async def login():
    try:
        auth_service: AuthService = await AuthService.create(None)
        return await auth_service.login()
    finally:
        auth_service.close()


@auth.post("/register")
async def register():
    try:
        auth_service: AuthService = await AuthService[AuthService].create()
        return await auth_service.register()
    finally:
        auth_service.close()


@auth.post("/logout")
async def logout():
    try:
        auth_service: AuthService = await AuthService[AuthService].create()
        return await auth_service.logout()
    finally:
        auth_service.close()