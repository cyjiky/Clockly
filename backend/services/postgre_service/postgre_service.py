from sqlalchemy.ext.asyncio import AsyncSession
from postgre import Base, User

from typing import TypeVar

M = TypeVar("M", bound=Base)


class PostgreService():
    def __init__(self, session: AsyncSession):
        self.__sesion = session

    async def commit(self) -> None:
        await self.__sesion.commit()

    async def flush(self) -> None:
        await self.__sesion.flush()

    async def flush_models(self, *models: Base) -> None:
        """Adds *models: Base to the session and flushes them"""
        self.__sesion.add_all(models)
        await self.flush()

    async def create_model(self, Model: M, **kwargs) -> M:
        return Model(**kwargs)
    
    async def get_user_by_username(self, username: str) -> User | None:
        pass

    async def get_user_by_email(self, email: str) -> User | None:
        pass

    # Юзера по его юзернейму
    # Все события юзера - все / на сегодня
    # Все задания юзера - все / на сегодня