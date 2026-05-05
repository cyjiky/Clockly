import json
import asyncio
import json
import asyncio
from datetime import datetime
from typing import AsyncGenerator, List
from postgre import Events, Tasks
from .calendar_service_shared import CoreServiceBaseSharedMethods

from config import settings


class ExportService(CoreServiceBaseSharedMethods):
    async def csv_historic_data_generator(
        self, user_id: str, start_date: datetime, end_date: datetime
    ) -> AsyncGenerator[str, None]:
        yield "id,name,descriprion,start_date,ent_date,full_day,calendar_id,complited\n"
        limit = settings.export_chunks_size

        while True:
            curr_chunk_counter = 0
            curr_chunk_csv = ""
            async for i in self._PostgreService.time_objects_range_generator(
                start_date, end_date, user_id
            ):
                row = f"{i['id']},{i['name']},{i['descriprion']},{i['start_date']},{i['ent_date']},{i['full_day']},{i['calendar_id']},{i['complited']}\n" # TODO

                curr_chunk_csv += curr_chunk_csv
                curr_chunk_counter += 1

                if curr_chunk_counter >= limit:
                    yield curr_chunk_csv
                    curr_chunk_csv = ""
                    curr_chunk_counter = 0

                yield row

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
                json_str = json.dumps(
                    record
                )  # TODO: convert to json export object via pydantic

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

            if curr_chunk_json:  # not empty check
                yield curr_chunk_json

            break

        yield "\n]"
