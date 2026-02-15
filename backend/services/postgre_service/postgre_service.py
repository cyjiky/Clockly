from sqlalchemy.ext.asyncio import AsyncSession

class PostgreService():
    def __init__(self, session: AsyncSession):
        self.__sesion = session

    async def commit(self) -> None:
        pass

    async def flush(self) -> None:
        pass

    async def close(self, commit: bool) -> None:
        pass
