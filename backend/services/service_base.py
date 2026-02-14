from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession


class CoreServiceBase:
    """
    To create 
    """
    def __init__(self):
        return self

    @classmethod
    async def create(cls, sqlalchemy_session: AsyncSession) -> CoreServiceBase:
        pass

    async def close(self) -> None:
        pass

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
