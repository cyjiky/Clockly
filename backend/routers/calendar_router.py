from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app_types import *
from DTOs import *
from postgre import Users, get_session_depends, merge_model
from auth.auth_utils import authorize_private_endpoint
from services import CalendarService

calendar = APIRouter()


@calendar.get("/object/{year}/{month}/{day}/{data_range}")
async def get_data_by_range(
    year: int,
    month: int,
    day: int,
    data_range: TimeLineEnum,
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends),
) -> ObjectsMonthData:
    calendar_service = await CalendarService.create(postgres_session)

    # No need to commit data to the database
    # Nothing changes
    try:
        user = await merge_model(user_, postgres_session)
        return await calendar_service.get_data_by_range(
            user_id=user.user_id,
            year=year,
            month=month,
            day=day,
            data_range=data_range,
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
    time_object_data: TimeObjectSchemeUpdate = Body(...),
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends),
) -> None:
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.change_time_object(
            user_id=user.user_id,
            time_object_id=object_id,
            time_object_type=time_object_type,
            time_object_data=time_object_data,
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
    postgres_session: AsyncSession = Depends(get_session_depends),
) -> None:
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.delete_time_object(
            time_object_type=time_object_type,
            object_id=object_id,
            user_id=user.user_id,
        )
        await calendar_service.close(commit=True)
    except Exception as e:
        await calendar_service.close(commit=False)
        raise e from e

@calendar.post("/calendar")
async def create_calendar(
    calendar_data: CalendarCreate,
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends),
) -> CalendarScheme:
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        out = await calendar_service.create_calendar(
            user_id=user.user_id,
            calendar_data=calendar_data
        )
        await calendar_service.close(commit=True)

        return out
    except Exception as e:
        await calendar_service.close(commit=False)
        raise e from e

@calendar.post("/task/{task_id}/{action}")
async def task_action(
    task_id: str,
    action: TaskActionEnum,
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends),
) -> None:
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.task_action(
            user_id=user.user_id, task_id=task_id, action=action
        )
        await calendar_service.close(commit=True)
    except Exception as e:
        await calendar_service.close(commit=False)
        raise e from e


@calendar.get("/task/{page}")
async def get_tasks(
    page: int = Path(..., ge=0.0),
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends)
) -> any: # TODO
    calendar_service = await CalendarService.create(postgres_session)
    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.get_tasks(user_id=user.user_id, page=page)
    except Exception as e:
        raise e from e    

@calendar.get("/calendar")
async def get_calendars(
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends),
) -> List[CalendarScheme]:
    calendar_service = await CalendarService.create(postgres_session)

    # No need to commit data to the database
    # Nothing changes
    try:
        user = await merge_model(user_, postgres_session)
        return await calendar_service.get_calendars(user_id=user.user_id)
    except Exception as e:
        raise e from e

@calendar.delete("/calendar/{calendar_id}")
async def delete_calendar(
    calendar_id: str,
    deletion_option: DeletionOptions = DeletionOptions.SET_NULL,
    user_: Users = Depends(authorize_private_endpoint),
    postgres_session: AsyncSession = Depends(get_session_depends)
) -> None:
    calendar_service = await CalendarService.create(postgres_session)

    try:
        user = await merge_model(user_, postgres_session)
        await calendar_service.delete_calendar(
            user_id=user.user_id,
            calendar_id=calendar_id
        )
        await calendar_service.close(commit=True)
    except Exception as e:
        await calendar_service.close(commit=True)
        raise e from e