import json
import asyncio
import json
import asyncio
from datetime import datetime
from typing import AsyncGenerator, List
from postgre import Events, Tasks
from .calendar_service_shared import CoreServiceBaseSharedMethods


class ExportService(CoreServiceBaseSharedMethods):
    async def csv_historic_data_generator(
        self, start_date: datetime, end_date: datetime
    ) -> AsyncGenerator[None, str]:
        yield "id,name,descriprion,start_date,ent_date,full_day,calendar_id,complited\n"
        offset = 0
        limit = 100  # TODO

        while True:
            for i in await self._PostgreService.time_objects_range_generator(start_date, end_date):
                row = f"{i['id']},{i['name']},{i['descriprion']},{i['start_date']},{i['ent_date']},{i['full_day']},{i['calendar_id']},{i['complited']}\n"
                yield row

            offset += limit

    async def json_historic_data_generator(
        self, start_date: datetime, end_date: datetime
    ) -> AsyncGenerator[None, str]:
        yield "[\n"

        offset = 0
        limit = 100
        is_first_record = True

        while True:
            for record in await self._PostgreService.time_objects_range_generator(start_date, end_date):
                json_str = json.dumps(record)

                if is_first_record:
                    yield f"  {json_str}"
                    is_first_record = False
                else:
                    yield f",\n  {json_str}"

            offset += limit

        yield "\n]"
