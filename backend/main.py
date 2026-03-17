from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine
import uvicorn

from contextlib import asynccontextmanager

from routers import *
from postgre import initialize_models, get_async_engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    """For async SQLalchemy models initialization"""

    engine = await get_async_engine()
    print(f"Got async engine: {type(engine)}")
    print("Initializing models")
    print(type(Base))
    await initialize_models(Base, engine)
    print("Models initialized")

    yield


app = FastAPI(lifespan=lifespan)

app.get("/")


def hello_world() -> str:
    return "Hello World!"


app.include_router(auth)
app.include_router(calendar)
app.include_router(chart)

# For debugging
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
