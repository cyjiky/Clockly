from typing import List, Tuple
from datetime import datetime

from services import CoreServiceBase
from DTOs import DayScheme
from app_types import *

from .calendar_service_shared import CoreServiceBaseSharedMethods

class VisualizationService(CoreServiceBaseSharedMethods):
    @staticmethod
    def _compute_scores(days: List[DayScheme]) -> None:
        pass

    @staticmethod
    def _get_time_range_borders(range: VisualizationTimeLineEnum | HeatMapTimeLineEnum) -> Tuple[datetime, datetime]:
        pass

    async def _get_time_objects_by_range(self, user_id: str, data_range: HeatMapTimeLineEnum | VisualizationTimeLineEnum):
        start, end = self._get_time_range_borders(data_range)
        objects = await self._PostgreService.get_time_objects_by_range(user_id=user_id, start_date=start, end_date=end)

    async def heat_map_by_score(self, user_id: str, data_range: HeatMapTimeLineEnum):
        start, end = self._get_time_range_borders(data_range)
        objects = await self._PostgreService.get_time_objects_by_range(user_id=user_id, start_date=start, end_date=end)

    async def pie_by_calendar(self, user_id: str, data_range: VisualizationTimeLineEnum):
        start, end = self._get_time_range_borders(data_range)
        objects = await self._PostgreService.get_time_objects_by_range(user_id=user_id, start_date=start, end_date=end)

    async def todays_pie_by_time_objects(self, user_id: str):
        start, end = self._get_time_range_borders(TimeLineEnum.DAY)
        objects = await self._PostgreService.get_time_objects_by_range(user_id=user_id, start_date=start, end_date=end)

    async def line_chart_by_score(self, user_id: str, data_range: VisualizationTimeLineEnum):
        start, end = self._get_time_range_borders(data_range)
        objects = await self._PostgreService.get_time_objects_by_range(user_id=user_id, start_date=start, end_date=end)