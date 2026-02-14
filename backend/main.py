from fastapi import FastAPI
from contextlib import asynccontextmanager

from routers import *
from postgre import initialize_models, Base

app = FastAPI()

app.get("/")
def hello_world() -> str:
    return "Hello World!"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """For async SQLalchemy models initialization"""
    await initialize_models(Base)

