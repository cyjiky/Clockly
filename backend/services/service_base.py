from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession

from .redis_service.redis_service import RedisService
from .postgre_service.postgre_service import PostgreService

from typing import TypeVar, Generic


class CoreServiceBase():
    def __init__(self, PostgreServiceInstance: PostgreService):
        self._PostgreService = PostgreServiceInstance


    @classmethod
    async def create(cls, sqlalchemy_session: AsyncSession):
        PostgreServiceInstance = PostgreService(sqlalchemy_session)

        return cls(PostgreServiceInstance)


    async def close(self, commit: bool) -> None:
        if commit:
            await self._PostgreService.commit()

# Planned to use in shortly future
# class CoreServiceCreationContextManager:
#     def __init__(self, CoreService: CoreServiceBase):
#         self.__CoreService = CoreService
    
#     @classmethod
#     def create(cls) -> CoreServiceCreationContextManager:
#         return cls()

#     def __aenter__(self):
#         pass

#     def __exit__(self):
#         pass
