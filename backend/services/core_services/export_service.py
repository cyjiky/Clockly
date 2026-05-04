from datetime import datetime
from typing import AsyncGenerator

from .calendar_service_shared import CoreServiceBaseSharedMethods

class ExportService(CoreServiceBaseSharedMethods):
    async def csv_historic_data_generator(self, start_date: datetime, end_date: datetime) -> AsyncGenerator[None, str]:
        pass

    async def json_historic_data_generator(self, start_date: datetime, end_date: datetime) -> AsyncGenerator[None, str]:
        pass