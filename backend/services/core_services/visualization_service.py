from typing import List
from datetime import datetime

from services import CoreServiceBase
from DTOs import DayScheme
from app_types import *

from .calendar_shared_methods_service_base import CoreServiceBaseSharedMethods

class VisualizationService(CoreServiceBaseSharedMethods):
    @staticmethod
    def compute_scores(days: List[DayScheme]) -> None:
        pass

    async def _get_time_objects_by_range(self, user_id: str, data_range: HeatMapTimeLineEnum | VisualizationTimeLineEnum):
        now = datetime.now()
        return await self.get_data_by_range(
            user_id=user_id,
            year=now.year,
            month=now.month,
            day=now.day,
            data_range=data_range
        )    

    async def heat_map_by_score(self, user_id: str, data_range: HeatMapTimeLineEnum):
        time_objects = await self._get_time_objects_by_range(
            user_id=user_id,
            data_range=data_range
        )


    async def pie_by_calendar(self, user_id: str, data_range: VisualizationTimeLineEnum):
        time_objects = await self._get_time_objects_by_range(
            user_id=user_id,
            data_range=data_range
        )

    async def todays_pie_by_time_objects(self, user_id: str, time_objects_type: BothTaskEventEnum):
        now = datetime.now()
        time_objects = await self._PostgreService.get_time_objects_by_date(
            user_id=user_id, date=now, time_objects_type=time_objects_type
        )

    async def line_chart_by_score(self, user_id: str, data_range: VisualizationTimeLineEnum):
        time_objects = await self._get_time_objects_by_range(
            user_id=user_id,
            data_range=data_range
        )