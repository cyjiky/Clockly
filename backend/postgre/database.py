from app_types import AppRunningMode
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from .models import Base

from typing import AsyncGenerator, TypeVar
import time

from config import settings
from logger import logger

engine: AsyncEngine = None


async def get_async_engine(mode: AppRunningMode = settings.app_mode) -> AsyncEngine:
    print("Initializing engine")

    for i in range(10):
        try:
            local_engine = create_async_engine(settings.get_postgres_dsn().unicode_string())
            async with local_engine.connect() as conn: 
                await conn.execute(
                    select(1)
                )
            return local_engine
        except SQLAlchemyError as e:
            if i == 0:
                logger.error(msg="Connection to the db is failed on app startup", exc_info=e)
            print(f"№{i} Connection to the db failed, retrying...")
            time.sleep(1)


async def get_async_sessionmaker(engine: AsyncEngine):
    return async_sessionmaker[AsyncSession](bind=engine, autoflush=False)


async def get_session_depends() -> AsyncGenerator[AsyncSession, None]:
    engine = await get_async_engine()
    ready_sessionmaker = await get_async_sessionmaker(engine)
    session = ready_sessionmaker()

    try:
        yield session
    finally:
        await session.aclose()


async def get_session() -> AsyncSession:
    engine = await get_async_engine(mode=settings.app_mode)
    ready_sessionmaker = await get_async_sessionmaker(engine)
    return ready_sessionmaker()


async def initialize_models(
    Base: DeclarativeBase, engine: AsyncEngine
) -> None:
    async with engine.connect() as conn:  # engine.connect() engine.begin()
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()


M = TypeVar("M", bound=Base)


async def merge_model(model: M, postgres_session: AsyncSession) -> M:
    """Use to merge model from diferent session"""
    return await postgres_session.merge(model)
