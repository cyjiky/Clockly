from fastapi import HTTPException

from uuid import uuid4

from DTOs import * # Optional 
from services import CoreServiceBase
from postgre import Tasks, Events

class CalendarService(CoreServiceBase):
    async def create_task(self, creds: Tasks):

        new_task_id = uuid4()
        new_task = Tasks(
            task_id=str(new_task_id),
            task_name=creds.task_name, 
            additional_deskription=creds.additional_description, 
            start_date=creds.start_date,
            end_date=creds.end_date
        )
        await self._PostgreService.flush_models(new_task)

    async def create_event(self, creds: Events):
        
        new_events_id = uuid4()
        new_event = Events(
            event_id=str(new_events_id), 
            event_name=creds.event_name, 
            additional_deskription=creds.additional_description, 
            start_date=creds.start_date,
            end_date=creds.end_date
        )
        await self._PostgreService.flush_models(new_event)
