from sqlalchemy.ext.asyncio import AsyncSession

class PostgreService():
    def __init__(self):
        pass

    async def commit(self) -> None:
        pass

    async def flush(self) -> None:
        pass

    async def close(self) -> None:
        pass
