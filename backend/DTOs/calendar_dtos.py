from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class CalendarCreate(BaseModel):
    name: str
    color: str


class CalendarScheme(CalendarCreate):
    calendar_id: str


class TimeObjectScheme(BaseModel):
    name: str
    description: Optional[str] = None

    start_date: datetime
    end_date: datetime

    fulL_day: bool

    calendar_id: Optional[
        str
    ] # If None, object will be assigned to user's
    # initial Calendar on object creation


class TimeObjectSchemeUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str] = None

    start_date: Optional[datetime]
    end_date: Optional[datetime]

    full_day: bool

    calendar_id: Optional[str]


class TaskSchemeOut(TimeObjectScheme):
    completed: bool
    calendar: Optional[CalendarScheme]


class EventSchemeOut(TimeObjectScheme):
    calendar: Optional[CalendarScheme]


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
    month_day: int
    special_events: List[SpecialEventScheme] = Field(default=[])
    objects: BothScheme


class ObjectsRangeData(BaseModel):
    month: int
    year: int
    data: List[DayScheme]


class RangeBody(BaseModel):
    start_time: datetime
    end_time: datetime
