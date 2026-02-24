from app_types import AppRunningMode
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_session,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)
from sqlalchemy import URL
from sqlalchemy.orm import DeclarativeBase

from dotenv import load_dotenv
import os
from typing import AsyncGenerator
import asyncio

load_dotenv()

APP_MODE = os.getenv("APP_MODE")

engine: AsyncEngine = None


async def get_async_engine(mode: AppRunningMode = APP_MODE) -> AsyncEngine:
    if engine:
        return engine

    username = os.getenv(
        "POSTGRE_PROD_USERNAME" if mode == "prod" else "POSTGRE_TEST_USERNAME"
    )
    password = os.getenv(
        "POSTGRE_PROD_PASSWORD" if mode == "prod" else "POSTGRE_TEST_PASSWORD"
    )
    host = os.getenv(
        "POSTGRE_PROD_HOST" if mode == "prod" else "POSTGRE_TEST_HOST"
    )
    database = os.getenv(
        "POSTGRE_PROD_DATABASE_NAME" if mode == "prod" else "POSTGRE_TEST_NAME"
    )
    port = os.getenv(
        "POSTGRE_PROD_PORT" if mode == "prod" else "POSTGRE_TEST_PORT"
    )

    url = (
        f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}"
    )

    print("Initialized engine")

    return create_async_engine(url)


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


async def initialize_models(
    Base: DeclarativeBase, engine: AsyncEngine
) -> None:
    async with engine.connect() as conn:  # engine.connect() engine.begin()
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
