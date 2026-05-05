from __future__ import annotations

from pydantic import BaseModel, model_validator, Field, ConfigDict
from pydantic.generics import GenericModel
from datetime import datetime
from typing import Optional, List, TypeVar, Generic, Literal
from ctypes import c_double


S = TypeVar("S", bound="VisualizationBase")


class TimeRangeBase(BaseModel):
    start_time: datetime
    end_time: datetime
    score: float
    color: Optional[str] = Field(default="#3498db")

    @model_validator(mode="after")
    def check_time_order(self):
        if self.end_time <= self.start_time:
            raise ValueError("end_time must be after start_time")
        return self


class ModelId(BaseModel):
    id: str


class TaskNames(BaseModel):
    name_task: str


class EventsNames(BaseModel):
    name_event: str


class LocationLine(BaseModel):
    horizontal_idx: str = Field(default=None)  # x


class PieSpaceOcupation(BaseModel):
    space_percentage: str


class VisualizationBase(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    visualization_name: str
    data_instances: List[VisualizationInstanceBase]


class VisualizationInstanceBase:
    pass


class TaskVisualizationLineChartInstance(
    VisualizationInstanceBase, TaskNames, LocationLine, ModelId, TimeRangeBase
):
    pass


class EventVisualizationLineChartInstance(
    VisualizationInstanceBase,
    EventsNames,
    LocationLine,
    ModelId,
    TimeRangeBase,
):
    pass


class TaskVisualizationPieInstance(
    VisualizationInstanceBase,
    TaskNames,
    PieSpaceOcupation,
    ModelId,
    TimeRangeBase,
):
    pass


class EventVisualizationPieInstance(
    VisualizationInstanceBase,
    EventsNames,
    PieSpaceOcupation,
    ModelId,
    TimeRangeBase,
):
    pass


class LineChartTasksScheme(
    VisualizationBase, TimeRangeBase, ModelId, TaskNames, LocationLine
):
    visualization_name: str = Field(default="Line Chart Tasks")
    data_instances: List[TaskVisualizationLineChartInstance]


class PieChartTasksScheme(
    VisualizationBase, TimeRangeBase, ModelId, TaskNames
):
    visualization_name: str = Field(default="Pie Chart Tasks")
    data_instances: List[TaskVisualizationPieInstance]


class LineChartEventsScheme(
    VisualizationBase, TimeRangeBase, ModelId, EventsNames, LocationLine
):
    visualization_name: str = Field(default="Line Chart Events")
    data_instances: List[EventVisualizationLineChartInstance]


class PieChartEventsScheme(
    VisualizationBase, TimeRangeBase, ModelId, EventsNames
):
    visualization_name: str = Field(default="Line Chart Events")
    data_instances: List[EventVisualizationPieInstance]


class LineChartScheme(GenericModel, Generic[S]):
    visualization_data: S
    range_start: datetime
    range_finish: datetime

    @model_validator(mode="after")
    def check_time_order(self):
        if not isinstance(S, VisualizationBase):
            raise ValueError(
                "Generic visualization type must inherit from VisualizationBase"
            )
        return self


class HeatMapScheme(BaseModel):
    heat_map: List[List[int]]
    type: Literal["tasks", "events", "both"]


class EventTrends(BaseModel):
    # Represents trend event name and frequency
    trends: List[str | int]
