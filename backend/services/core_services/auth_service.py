from services import CoreServiceBase

from DTOs import LoginBody, RegisterBody

class AuthService(CoreServiceBase):
    async def login(self, creds: LoginBody):
        pass

    async def register(self, cred: RegisterBody):
        pass

    async def logout(self):
        pass

    async def change_username(self):
        pass

    async def change_password(self):
        pass