from fastapi import FastAPI
from contextlib import asynccontextmanager

from routers import *

app = FastAPI()

app.get("/")
def hello_world() -> str:
    return "Hello World!"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """For Postgre model async initialization"""

