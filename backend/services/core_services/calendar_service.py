from fastapi import HTTPException

from uuid import uuid4

from DTOs import *  # Optional
from services import CoreServiceBase
from postgre import Tasks, Events, Users, Calendars
from app_types import *

from typing import Dict

class CalendarService(CoreServiceBase):
    @staticmethod
    def map_weekdays_to_readable(weekday: int) -> str:
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekdays[weekday % 7]

    async def _define_calendar_id(
        self, provided_calendar_id: str | None,
        user_id: str
    ) -> str:
        if not provided_calendar_id:
            initial_calendar = await self._PostgreService.get_user_initial_calendar(user_id)
            provided_calendar_id = initial_calendar.calendar_id

        return provided_calendar_id

    async def _create_task(self, user_id: str, task_data: TimeObjectScheme) -> None:
        defined_calendar_id = await self._define_calendar_id(task_data.calendar_id, user_id)

        new_task_id = str(uuid4())
        new_task = Tasks(
            task_id=new_task_id,
            name=task_data.name,
            additional_description=task_data.description,
            start_date=task_data.start_date,
            end_date=task_data.end_date,
            calendar_id=defined_calendar_id,
            user_id=user_id
        )
        await self._PostgreService.flush_models(new_task)

    async def _create_event(self, user_id: str, event_data: TimeObjectScheme) -> None:
        defined_calendar_id = await self._define_calendar_id(event_data.calendar_id, user_id)
        print("creating model")
        new_events_id = str(uuid4())
        new_event = Events(
            event_id=new_events_id,
            name=event_data.name,
            additional_description=event_data.description,
            start_date=event_data.start_date,
            end_date=event_data.end_date,
            calendar_id=defined_calendar_id,
            user_id=user_id
        )
        print("flushing model")
        await self._PostgreService.flush_models(new_event)

    async def create_time_object(self, user_id: str, object_type: TimeObjectsEnum, object_data: TimeObjectScheme) -> None:
        match object_type:
            case TimeObjectsEnum.TASK:
                await self._create_task(
                    user_id=user_id,
                    task_data=object_data
                )
            case TimeObjectsEnum.EVENT:
                await self._create_event(
                    user_id=user_id,
                    event_data=object_data
                )

    async def create_calendar(self, user_id: str, creds: CalendarScheme) -> None:
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
            user_id=user_id
        )

        await self._PostgreService.flush_models(new_event)

    async def change_task(self, user_id: str, task_id: str, creds: TimeObjectScheme) -> None:

        db_task = await self._PostgreService.get_task(
            task_id=task_id,
        )
        if not db_task:
            raise ValueError(f"Task with id {task_id} not found")

        if db_task.user_id != user_id:
            raise ValueError(
                detail=f"Oh noooo, Mashellaaa.. :(",
            )
        
        db_task.additional_description=creds.description
        db_task.start_date=creds.start_date
        db_task.end_date=creds.end_date
        db_task.calendar_id=creds.calendar

        await self._PostgreService.flush() 

    async def change_event(self, user_id: str, event_id: str, creds: TimeObjectsEnum) -> None:

        db_task = await self._PostgreService.get_event(
            event_id=event_id, 
        )

        if not db_task:
            raise ValueError(f"Task with id {event_id} not found")

        if db_task.user_id != user_id:
            raise ValueError(
                detail=f"Oh noooo, Mashellaaa.. :(",
            )
        
        db_task.additional_description=creds.description
        db_task.start_date=creds.start_date
        db_task.end_date=creds.end_date
        db_task.calendar_id=creds.calendar

        await self._PostgreService.flush() 

    async def delete_task(self, user_id: str, task_id: str) -> None:
        pass

    async def delete_event(self, user_id: str, event_id: str) -> None:
        pass


    async def task_action(self, user_id: str, task_id: str, action: TaskActionEnum) -> None:
        pass

    async def get_month_data(self, user_id: str) -> ObjectsMonthDataScheme:
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


        return ObjectsMonthDataScheme(
            month=curr_datetime.month,
            year=curr_datetime.year,
            data=[DayScheme(
                day_of_week_readable=self.map_weekdays_to_readable(datetime(
                    year=curr_datetime.year,
                    month=curr_datetime.month,
                    day=month_day
                ).weekday),
                special_events=[],
                objects=objects
            ) for month_day, objects in objects_by_days.items()]
        )
