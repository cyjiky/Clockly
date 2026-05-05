import json
import asyncio
import json
import asyncio
from datetime import datetime
from typing import AsyncGenerator, List
from postgre import Events, Tasks
from .calendar_service_shared import CoreServiceBaseSharedMethods

from DTOs import ExportJSONOBject

from config import settings


class ExportService(CoreServiceBaseSharedMethods):
    async def csv_historic_data_generator(
        self, user_id: str, start_date: datetime, end_date: datetime
    ) -> AsyncGenerator[str, None]:
        yield "object_type,id,name,descriprion,start_date,ent_date,full_day,calendar_id,complited\n"
        limit = settings.export_chunks_size

        while True:
            curr_chunk_counter = 0
            curr_chunk_csv = ""

            async for i in self._PostgreService.time_objects_range_generator(
                start_date, end_date, user_id
            ):
                completed_field_value = (
                    None if isinstance(i, Events) else i.completed
                )
                row = f"{"event" if isinstance(i, Events) else "task"},{i.id},{i.name},{i.additional_description},{i.start_date},{i.end_date},{i.full_day},{i.calendar_id},{completed_field_value}\n"

                curr_chunk_csv += row
                curr_chunk_counter += 1

                if curr_chunk_counter >= limit:
                    yield curr_chunk_csv
                    curr_chunk_csv = ""
                    curr_chunk_counter = 0

                    await asyncio.sleep(1) # for realistic delay

            break

        if curr_chunk_csv:  # not empty check
            yield curr_chunk_csv

    async def json_historic_data_generator(
        self, user_id: str, start_date: datetime, end_date: datetime
    ) -> AsyncGenerator[str, None]:
        yield "[\n"

        limit = settings.export_chunks_size
        is_first_record = True

        while True:
            curr_chunk_counter = 0
            curr_chunk_json = ""
            async for (
                record
            ) in self._PostgreService.time_objects_range_generator(
                start_date, end_date, user_id
            ):
                completed_field_value = (
                    None if isinstance(record, Events) else record.completed
                )
                pydantic_mapped = ExportJSONOBject(
                    object_type=(
                        "event" if isinstance(record, Events) else "task"
                    ),
                    id=record.id,
                    name=record.name,
                    description=record.additional_description,
                    start_date=record.start_date,
                    end_date=record.end_date,
                    full_day=record.full_day,
                    calendar_id=record.calendar_id,
                    completed=completed_field_value,
                )
                json_str = pydantic_mapped.model_dump_json(indent=2)
                if is_first_record:
                    curr_chunk_json += f"  {json_str}"
                    is_first_record = False
                else:
                    curr_chunk_json += f",\n  {json_str}"

                curr_chunk_counter += 1

                if curr_chunk_counter >= limit:
                    yield curr_chunk_json
                    curr_chunk_json = ""
                    curr_chunk_counter = 0

                    await asyncio.sleep(0.2) # for realistic delay

            if curr_chunk_json:  # not empty check
                yield curr_chunk_json

            break

        yield "\n]"
