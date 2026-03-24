from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from app_types import *
from DTOs import *
from postgre import Users, get_session_depends, merge_model
from auth.auth_utils import authorize_private_endpoint
from services import CalendarService

calendar = APIRouter()


# @calendar.get("/task/summary/{id}")
# async def summary_task(start_time: str, end_time: str):
#     pass

@calendar.get("/object/")
async def get_month_data(
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends)
) -> ObjectsMonthData:
    calendar_service = await CalendarService.create(postgres_session)

    # No need to commit data to the database
    # Nothing changes
    try:
        user = await merge_model(user_, postgres_session)
        return await calendar_service.get_month_data(
            user_id=user.user_id
        )
    except Exception as e:
        raise e from e

@calendar.post("/object/{time_object_type}")
async def create_time_object(
    time_object_type: TimeObjectsEnum,
    time_object_data: TimeObjectSchemeCreate,
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends),
) -> None:
    """Pass datetimes without timezone Z flag!"""
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.create_time_object(
            user_id=user.user_id,
            object_type=time_object_type,
            object_data=time_object_data,
        )
        await calendar_service.close(commit=True)
    except Exception as e:
        await calendar_service.close(commit=False)
        raise e from e


@calendar.patch("/object/{time_object_type}/{object_id}")
async def update_object(
    time_object_type: TimeObjectsEnum,
    object_id: str,
    time_object_data: TimeObjectSchemeCreate = Body(...),
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends)
) -> None:
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.change_time_object(
            user_id=user.user_id,
            time_object_id=object_id,
            time_object_type=time_object_type,
            object_data=time_object_data, 
        )
        await calendar_service.close(commit=True)
    except Exception as e:
        await calendar_service.close(commit=False)
        raise e from e

@calendar.post("/object/{time_object_type}/delete/{object_id}")
async def delete_object(
    time_object_type: TimeObjectsEnum,
    object_id: str,
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends)
) -> None:
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.delete_object(
            time_object_type=time_object_type,
            object_id=object_id,
            user_id=user.user_id
        )
        await calendar_service.close(commit=True)
    except Exception as e:
        await calendar_service.close(commit=False)
        raise e from e

@calendar.post("/task/complete/{task_id}")
async def completed_task(
    task_id: str,
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends)
):
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.complete_task(
            user_id=user.user_id,
            task_id=task_id
        )
        await calendar_service.close(commit=True)
    except Exception as e:
        await calendar_service.close(commit=False)
        raise e from e

@calendar.post("/task/cancel/{task_id}")
async def cancel_task(
    task_id: str, 
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends)
) -> None:
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.cancel_task(
            user_id=user.user_id,
            task_id=task_id
        )
        await calendar_service.close(commit=True)
    except Exception as e:
        await calendar_service.close(commit=False)
        raise e from e

@calendar.get("/task/unfulfilled/{task_id}")
async def unfulfilled_tasks(
    task_id: str,
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends)
):  # TODO
    calendar_service = await CalendarService.create(postgres_session)

    # No need to commit data to the database
    # Nothing changes
    try:
        user = await merge_model(user_, postgres_session)
        return await calendar_service.get_unfulfilled_tasks(
            user_id=user.user_id,
            task_id=task_id
        )
    except Exception as e:
        raise e from e

