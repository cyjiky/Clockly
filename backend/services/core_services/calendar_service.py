from fastapi import HTTPException

from uuid import uuid4

from DTOs import *  # Optional
from services import CoreServiceBase
from postgre import Tasks, Events, Users, Calendars
from app_types import *

from datetime import datetime
from typing import Dict


class CalendarService(CoreServiceBase):
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
        match object_type:
            case TimeObjectsEnum.TASK:
                await self._create_task(user_id=user_id, task_data=object_data)
            case TimeObjectsEnum.EVENT:
                await self._create_event(
                    user_id=user_id, event_data=object_data
                )

    async def create_calendar(
        self, user_id: str, creds: CalendarScheme
    ) -> None:
        potential_calendar = (
            await self._PostgreService.get_user_initial_calendar(
                user_id=user_id
            )
        )

        new_calendar_id = str(uuid4())
        new_event = Calendars(
            calendar_id=new_calendar_id,
            calendar_name=creds.name,
            color=creds.color,
            is_initial=False if potential_calendar else True,
            user_id=user_id,
        )

        await self._PostgreService.flush_models(new_event)

    async def change_time_object(
        self,
        user_id: str,
        time_object_id: str,
        time_object_data: TimeObjectScheme,
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
            raise ValueError(
                f"{time_object_type.value.title()} with id {time_object_id} not found"
            )

        if time_object.user_id != user_id:
            raise HTTPException(status_code=401, detail="Unauthorized")

        time_object.name = time_object_data.name
        time_object.additional_description = time_object_data.description
        time_object.start_date = time_object_data.start_date
        time_object.end_date = time_object_data.end_date

        # We won't change object's calendar if no calendar_id is being passed
        # Because calendar_id is optional
        if time_object_data.calendar_id:
            time_object.calendar_id = time_object_data.calendar_id

        await self._PostgreService.flush()

    async def delete_task(self, user_id: str, task_id: str) -> None:
        pass

    async def delete_object(self, user_id: str, event_id: str) -> None:
        pass

    async def task_action(
        self, user_id: str, task_id: str, action: TaskActionEnum
    ) -> None:
        pass

    async def get_month_data(self, user_id: str) -> ObjectsMonthData:
        curr_datetime = datetime.now()
        objects = await self._PostgreService.get_by_range(
            user_id=user_id,
            curr_datetime=curr_datetime,
            timerange=TimeLineEnum.MONTH,
        )

        objects_by_days: Dict[int, BothScheme] = {}

        for object in objects:
            day_objects = objects_by_days.setdefault(
                object.start_date.day, BothScheme()
            )
            if isinstance(object, Events):
                day_objects.events.append(
                    EventSchemeOut(
                        name=object.name,
                        description=object.description,
                        start_date=object.start_date,
                        end_date=object.end_date,
                        calendar=CalendarScheme.model_validate(
                            object.calendar, from_attributes=True
                        ),
                    )
                )
            else:
                day_objects.tasks.append(
                    TaskSchemeOut(
                        name=object.name,
                        description=object.description,
                        start_date=object.start_date,
                        end_date=object.end_date,
                        calendar=CalendarScheme.model_validate(
                            object.calendar, from_attributes=True
                        ),
                        completed=object.completed,
                    )
                )

            objects_by_days[object.start_date.day] = day_objects

        return ObjectsMonthData(
            month=curr_datetime.month,
            year=curr_datetime.year,
            data=[
                DayScheme(
                    day_of_week_readable=self.map_weekdays_to_readable(
                        datetime(
                            year=curr_datetime.year,
                            month=curr_datetime.month,
                            day=month_day,
                        ).weekday
                    ),
                    special_events=[],
                    objects=objects,
                )
                for month_day, objects in objects_by_days.items()
            ],
        )
