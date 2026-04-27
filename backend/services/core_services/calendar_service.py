from fastapi import HTTPException

from uuid import uuid4

from DTOs import *  # Optional
from services import CoreServiceBase
from postgre import Tasks, Events, Calendars
from app_types import *

from .calendar_shared_methods_service_base import CoreServiceBaseSharedMethods

from datetime import datetime, timedelta, time


class CalendarService(CoreServiceBaseSharedMethods):
    @staticmethod
    def map_weekdays_to_readable(weekday: int) -> str:
        weekdays = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        return weekdays[weekday % 7]

    @staticmethod
    def _validate_start_end_date(
        start_date: datetime, end_date: datetime
    ) -> bool:
        return (end_date - start_date) > timedelta(minutes=1)

    async def _define_calendar_id(
        self, provided_calendar_id: str | None, user_id: str
    ) -> str:
        if not provided_calendar_id:
            initial_calendar = (
                await self._PostgreService.get_user_initial_calendar(user_id)
            )
            provided_calendar_id = initial_calendar.calendar_id

        return provided_calendar_id

    async def _create_task(
        self, user_id: str, task_data: TimeObjectScheme
    ) -> None:
        defined_calendar_id = await self._define_calendar_id(
            task_data.calendar_id, user_id
        )

        new_task_id = str(uuid4())
        new_task = Tasks(
            id=new_task_id,
            name=task_data.name,
            additional_description=task_data.description,
            start_date=task_data.start_date,
            end_date=task_data.end_date,
            full_day=task_data.fulL_day,
            calendar_id=defined_calendar_id,
            user_id=user_id,
            completed=False,
        )
        await self._PostgreService.flush_models(new_task)

    async def _create_event(
        self, user_id: str, event_data: TimeObjectScheme
    ) -> None:
        defined_calendar_id = await self._define_calendar_id(
            event_data.calendar_id, user_id
        )
        print("creating model")
        new_events_id = str(uuid4())
        new_event = Events(
            id=new_events_id,
            name=event_data.name,
            additional_description=event_data.description,
            start_date=event_data.start_date,
            end_date=event_data.end_date,
            full_day=event_data.fulL_day,
            calendar_id=defined_calendar_id,
            user_id=user_id,
        )
        print("flushing model")
        await self._PostgreService.flush_models(new_event)

    async def create_time_object(
        self,
        user_id: str,
        object_type: TimeObjectsEnum,
        object_data: TimeObjectScheme,
    ) -> None:
        if not self._validate_start_end_date(
            start_date=object_data.start_date, end_date=object_data.end_date
        ):
            raise HTTPException(
                status_code=400,
                detail="Time object start date must be less than end date, at least one minute difference",
            )

        # Prunning time parts since object duration is full day
        if object_data.fulL_day:
            object_data.start_date = object_data.start_date.date
            object_data.end_date = object_data.end_date.date

        match object_type:
            case TimeObjectsEnum.TASK:
                await self._create_task(user_id=user_id, task_data=object_data)
            case TimeObjectsEnum.EVENT:
                await self._create_event(
                    user_id=user_id, event_data=object_data
                ) 

    async def create_calendar(
        self, user_id: str, calendar_data: CalendarCreate
    ) -> CalendarScheme:
        potential_calendar = (
            await self._PostgreService.get_user_initial_calendar(
                user_id=user_id
            )
        )

        potential_existing_calendar = (
            await self._PostgreService.get_user_calendar_by_name(
                user_id=user_id, calendar_name=calendar_data.name
            )
        )

        if potential_existing_calendar:
            raise HTTPException(
                status_code=400,
                detail="Calendar with this name already exists",
            )

        new_calendar_id = str(uuid4())
        new_calendar = Calendars(
            calendar_id=new_calendar_id,
            name=calendar_data.name,
            color=calendar_data.color,
            is_initial=False if potential_calendar else True,
            user_id=user_id,
        )

        await self._PostgreService.flush_models(new_calendar)

        return CalendarScheme.model_validate(
            new_calendar, from_attributes=True
        )

    async def change_time_object(
        self,
        user_id: str,
        time_object_id: str,
        time_object_data: TimeObjectSchemeUpdate,
        time_object_type: TimeObjectsEnum,
    ) -> None:

        match time_object_type:
            case TimeObjectsEnum.TASK:
                time_object = await self._PostgreService.get_task_by_id(
                    task_id=time_object_id,
                )
            case TimeObjectsEnum.EVENT:
                time_object = await self._PostgreService.get_event_by_id(
                    event_id=time_object_id,
                )

        if not time_object:
            raise HTTPException(
                status_code=400,
                detail=f"{time_object_type.value.title()} with id {time_object_id} not found",
            )

        if time_object.user_id != user_id:
            raise HTTPException(status_code=401, detail="Unauthorized")

        updated_start_date = (
            time_object_data.start_date or time_object.start_date
        )
        updated_end_date = time_object_data.end_date or time_object.end_date

        if not self._validate_start_end_date(
            start_date=updated_start_date, end_date=updated_end_date
        ):
            raise HTTPException(
                status_code=400,
                detail="Time object start date must be less than end date, at least one minute difference",
            )

        if time_object_data.calendar_id:
            if not await self._PostgreService.get_calendar_by_id(
                user_id=user_id, calendar_id=object
            ):
                raise HTTPException(
                    status_code=400, detail="This calendar doesn't exist"
                )

        time_object.name = time_object_data.name or time_object.name
        time_object.additional_description = (
            time_object_data.description or time_object.additional_description
        )
        time_object.start_date = updated_start_date
        time_object.end_date = updated_end_date
        time_object.calendar_id = (
            time_object_data.calendar_id or time_object.calendar_id
        )

        await self._PostgreService.flush()

    async def delete_time_object(
        self, user_id: str, object_id: str, time_object_type: TimeObjectsEnum
    ) -> None:
        match time_object_type:
            case TimeObjectsEnum.TASK:
                task = await self._PostgreService.get_task_by_id(object_id)
                if task and task.user_id == user_id:
                    await self._PostgreService.delete_task(object_id)
                else:
                    raise HTTPException(
                        status_code=400,
                        detail="This task does not exist",
                    )
            case TimeObjectsEnum.EVENT:
                event = await self._PostgreService.get_event_by_id(object_id)
                if event and event.user_id == user_id:
                    await self._PostgreService.delete_event(object_id)
                else:
                    raise HTTPException(
                        status_code=400,
                        detail="This event does not exist",
                    )

    async def task_action(
        self, user_id: str, task_id: str, action: TaskActionEnum
    ) -> None:
        task = await self._PostgreService.get_task_by_id(task_id=task_id)

        if not task:
            raise HTTPException(
                status_code=400, detail="This task does not exist"
            )

        if task.user_id != user_id:
            raise HTTPException(
                status_code=400, detail="This task does not exist"
            )

        match action:
            case TaskActionEnum.COMPLETE:
                task.completed = True
            case TaskActionEnum.INCOMPLETE:
                task.completed = False

    # ----- TODO ------

    async def get_tasks(self, user_id: str, page: int) -> List[Tasks]:
        """Page must greater or equal 0"""
        if page <= 0:
            raise HTTPException(
                status_code=400, detail="Page must be greater or equal 0"
            )
        try:
            tasks = await self._PostgreService.get_tasks_by_userId(
                user_id=user_id, page=page
            )
        except Exception as e:
            raise HTTPException(status_code=404, detail="User or tasks not found")
        
        return [
                Tasks.model_validate(task, from_attributes=True)
                for task in tasks
            ]

    # -----------------

    async def get_calendars(self, user_id: str) -> List[CalendarScheme]:
        calendars = await self._PostgreService.get_user_calendars(
            user_id=user_id
        )

        return [
            CalendarScheme.model_validate(calendar, from_attributes=True)
            for calendar in calendars
        ]

    async def delete_calendar(
        self, user_id: str, calendar_id: str, deletion_option: DeletionOptions
    ) -> None:
        calendar = await self._PostgreService.get_calendar_by_id(
            user_id=user_id, calendar_id=calendar_id
        )

        if not calendar:
            raise HTTPException(
                status_code=400, detail="This calendar doesn't exist"
            )

        if calendar.is_initial:
            raise HTTPException(
                status_code=400, detail="You can't delete initial calendar!"
            )

        match deletion_option:
            case DeletionOptions.CASCADE:
                await self._PostgreService.delete_calendar_time_objects(
                    user_id=user_id, calendar_id=calendar_id
                )
            case DeletionOptions.SET_NULL:
                await self._PostgreService.remove_time_objects_calendar(
                    user_id=user_id, calendar_id=calendar_id
                )
