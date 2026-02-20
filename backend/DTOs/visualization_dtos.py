from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional, List

class TimeRangeBase(BaseModel):
    start_time: datetime
    end_time: datetime
    score: List[float]
    color: Optional[str] = "#3498db"

    @model_validator(mode='after')
    def check_time_order(self):
        if self.end_time <= self.start_time:
            raise ValueError("end_time must be after start_time")
        return self

class ModelId(BaseModel):
    id: int 

class TaskNames(BaseModel):
    name_task: str 

class EventsNames(BaseModel):
    name_event: str 

class LocationLine(BaseModel):
    location: Optional[str] = None # x 

class LineChartTasksScheme(TimeRangeBase, ModelId, TaskNames, LocationLine):
    pass
 
class PieChartTasksScheme(TimeRangeBase, ModelId, TaskNames):
    pass

class LineChartEventsScheme(TimeRangeBase, ModelId, EventsNames, LocationLine):
    pass 

class PieChartEventsScheme(TimeRangeBase, ModelId, EventsNames):
    pass
