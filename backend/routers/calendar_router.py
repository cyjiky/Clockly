from fastapi import FastAPI
from fastapi import APIRouter

auth = APIRouter()

# Tasks
@auth.post("/create_task")
def new_task_create():
    pass

@auth.post("/change_task")
def update_task():
    pass

@auth.post("/delete_task")
def delete_task():
    pass

@auth.post("/delete_task")
def delete_task():
    pass

# Event 
@auth.post("/create_event")
def create_event():
    pass 

@auth.post("/change_event")
def change_event():
    pass 

@auth.post("/delete_event")
def delete_event():
    pass 