from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from app_types import *
from DTOs import *
from postgre import Users, get_session_depends, merge_model
from auth.auth_utils import authorize_private_endpoint
from services import CalendarService

calendar = APIRouter()

@calendar.get("/task/summary/{id}")
async def summary_task(start_time: str, end_time: str):
    pass


@calendar.post("/object/{time_object_type}")
async def create_time_object(
    time_object_type: TimeObjectsEnum,
    time_object_data: TimeObjectScheme,
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends)
) -> None:
    """Pass datetimes without timezone Z flag!"""
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.create_time_object(
            user_id=user.user_id,
            object_type=time_object_type,
            object_data=time_object_data
        )
        await calendar_service.close(commit=True)
    except Exception as e:
        await calendar_service.close(commit=False)
        raise e from e


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
