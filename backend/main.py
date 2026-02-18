from fastapi import FastAPI
from contextlib import asynccontextmanager

from routers import *
from postgre import *

app = FastAPI()

app.get("/")
def hello_world() -> str:
    return "Hello World!"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """For async SQLalchemy models initialization"""
    engine = await get_async_engine()
    await initialize_models(Base, engine=engine)

app.include_router(auth)
app.include_router(calendar)
app.include_router(chart)