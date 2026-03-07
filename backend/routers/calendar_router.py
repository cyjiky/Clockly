from fastapi import APIRouter
from app_types import *
from DTOs import RangeBody

calendar = APIRouter()


# Tasks
@calendar.get("/task/summary/{id}")
def summary_task(start_time: str, end_time: str):
    pass


# Tasks
@calendar.post("/task")
def new_task_create():
    pass


@calendar.patch("/task/{id}")
def update_task(id: int):
    pass


@calendar.post("/task/delete/{id}")
def delete_task(id: int):
    pass


@calendar.post("/task/completed/{id}")
def completed_task(id: int):
    pass


@calendar.post("/task/canceled/{id}")
def canceled_task(id: int):
    pass


@calendar.delete("/task/delete/{id}")
def delete_task(id: int):
    pass


# Event
@calendar.post("/event")
def create_event():
    pass


@calendar.patch("/event/{id}")
def change_event(id: int):
    pass


@calendar.post("event/unfulfilled/{id}")
def unfulfilled_event(id: int):
    pass


@calendar.delete("/event/delete/{id}")
def delete_event(id: int):
    pass 

@calendar.get("/history")
def history_tasks_or_event(
    type: BothTaskEventEnum, 
    range: RangeBody
):
    pass
