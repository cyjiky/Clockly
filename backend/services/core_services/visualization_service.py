from typing import List
from datetime import datetime

from services import CoreServiceBase
from DTOs import DayScheme
from app_types import *

class VisualizationService(CoreServiceBase):
    @staticmethod
    def compute_scores(days: List[DayScheme]) -> None:
        pass

    def heat_map_by_score(self, user_id: str, range: HeatMapTimeLineEnum):
        pass

    def pie_by_calendar(self, user_id: str, range: VisualizationTimeLineEnum):
        pass

    def todays_pie_by_time_objects(self, user_id: str, today: datetime, time_objects: BothTaskEventEnum):
        pass

    def line_chart_by_score(self, user_id: str, range: VisualizationTimeLineEnum):
        pass