from fastapi import HTTPException

from uuid import uuid4

from DTOs import * # Optional 
from services import CoreServiceBase
from postgre import Tasks, Events

class CalendarService(CoreServiceBase):
    async def _define_calendar_id(self, provided_calendar_id: str | None) -> str:
        if not provided_calendar_id:
            initial_calendar = await self._PostgreService.get_user_initial_calendar()
            provided_calendar_id = initial_calendar.calendar_id

        return provided_calendar_id

    async def create_task(self, creds: TaskScheme):
        defined_calendar_id = await self._define_calendar_id(creds.calendar_id)

        new_task_id = uuid4()
        new_task = Tasks(
            task_id=str(new_task_id),
            task_name=creds.task_name, 
            additional_deskription=creds.additional_description, 
            start_date=creds.start_date,
            end_date=creds.end_date,
            calendar_id=defined_calendar_id
        )
        await self._PostgreService.flush_models(new_task)


    async def create_event(self, creds: EventScheme):
        defined_calendar_id = await self._define_calendar_id(creds.calendar_id)
                
        new_events_id = uuid4()
        new_event = Events(
            event_id=str(new_events_id), 
            event_name=creds.event_name, 
            additional_deskription=creds.additional_description, 
            start_date=creds.start_date,
            end_date=creds.end_date,
            calendar_id=defined_calendar_id
        )

        await self._PostgreService.flush_models(new_event)

    async def create_calendar(self, creds: CalendarScheme):     
        potential_calendar = await self._PostgreService.get_user_initial_calendar()

        new_calendar_id = uuid4()
        new_event = Events(
            calendar_id=str(new_calendar_id),
            calendar_name=creds.name,
            color=creds.color,
            is_initial=False if potential_calendar else True
        )

        await self._PostgreService.flush_models(new_event)

    async def change_task():
        pass

    async def change_event():
        pass

    async def get_by_range():
        pass