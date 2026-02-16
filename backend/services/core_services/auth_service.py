from services import CoreServiceBase

from DTOs import LoginBody, RegisterBody

from postgre import User
from typing import Optional
import auth as auth_utils

from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4
import os

class AuthService(CoreServiceBase):

    async def register(self, cred: RegisterBody):
        auth_utils.validate_email(cred.email)
        auth_utils.validate_password(cred.password)

        if await self._PostgresService.get_user_by_username_or_email(
            username=cred.username, 
            email=cred.email):
            raise ValueError

        new_user = User(
            user_id=str(uuid4()),
            username = cred.username, 
            email = cred.email, 
            password_hash = auth_utils.hash_password(cred.password)
        )
        await self._PostgresService(new_user)
        return None


    async def login(self, cred: LoginBody):
        potencial_user:User = await self._PostgreService.get_user_by_username_or_email(
            username=cred.username, 
            email=None)
        
        if not potencial_user:
            raise ValueError
        
        return None 

    async def logout(self):
        pass

    async def change_username(self):
        pass

    async def change_password(self):
        pass