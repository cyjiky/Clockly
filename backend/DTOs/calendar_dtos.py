from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class CalendarScheme(BaseModel):
    calendar_id: str
    name: str
    color: str


class TimeObjectScheme(BaseModel):
    name: str
    description: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    calendar_id: Optional[
        str
    ]  # If None, will be assigned to user's initial Calendar


class TaskSchemeOut(TimeObjectScheme):
    completed: bool
    calendar: CalendarScheme

class EventSchemeOut(TimeObjectScheme):
    calendar: CalendarScheme


class BothScheme(BaseModel):
    events: List[EventSchemeOut] = Field(default=[])
    tasks: List[TaskSchemeOut] = Field(default=[])


class SpecialEventScheme(BaseModel):
    name: str
    description: Optional[str] = Field(default=None)
    date: datetime
    color: str


class DayScheme(BaseModel):
    # month: int
    day_of_week_readable: str
    special_events: List[SpecialEventScheme] = Field(default=[])
    objects: BothScheme


class ObjectsMonthDataScheme(BaseModel):
    month: int
    year: int
    data: List[DayScheme]


class RangeBody(BaseModel):
    start_time: datetime
    end_time: datetime