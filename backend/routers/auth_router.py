from fastapi import FastAPI
from fastapi import APIRouter

auth = APIRouter()

@auth.post("/login")
def login():
    pass 

@auth.post("/register")
def register():
    pass 

@auth.post("/logout")
def logout():
    pass