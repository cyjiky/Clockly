from app_types import AppRunningMode
from sqlalchemy.ext.asyncio import create_async_engine, async_session, AsyncSession, AsyncEngine
from sqlalchemy import URL
from sqlalchemy.orm import DeclarativeBase

from dotenv import load_dotenv
import os
from typing import AsyncGenerator
import asyncio

load_dotenv()

APP_MODE = os.getenv("APP_MODE")

async def get_async_engine(mode: AppRunningMode = APP_MODE) -> AsyncEngine:
    url = URL(
        "postgresql+asyncpg",
        username=os.getenv("POSTGRE_PROD_USERNAME" if mode == "prod" else "POSTGRE_TEST_USERNAME"),
        password=os.getenv("POSTGRE_PROD_PASSWORD" if mode == "prod" else "POSTGRE_TEST_PASSWORD"),
        host=os.getenv("POSTGRE_PROD_HOST" if mode == "prod" else "POSTGRE_TEST_HOST"),
        database=os.getenv("POSTGRE_PROD_DATABASE_NAME" if mode == "prod" else "POSTGRE_TEST_NAME"),
    )

    engine = await create_async_engine(
        url=url,
        echo=True
    )

    return engine

async def get_session_depends() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = async_session()
    try:
        yield session
    finally:
        await session.aclose()

async def initialize_models(Base: DeclarativeBase, engine: AsyncEngine = get_async_engine()) -> None:
    async with engine.connect() as conn:
        conn.run_sync(Base.metadata.create_all(engine))
