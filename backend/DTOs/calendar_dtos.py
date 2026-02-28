from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CalendarScheme(BaseModel):
    calendar_id: str
    name: str
    color: str


class TaskScheme(BaseModel):
    name: str
    description: Optional[str] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    calendar_id: Optional[
        str
    ]  # If None, will be assigned to user's initial Calendar


class EventScheme(BaseModel):
    name: str
    description: Optional[str] = None

    start_date: datetime
    end_date: Optional[datetime] = None
    calendar_id: Optional[
        str
    ]  # If None, will be assigned to user's initial Calendar

    # repeat_days: List[str] = []
    # repeat_time: List[datetime] = []


class BothScheme(BaseModel):
    Events: List[EventScheme] = None
    Tasks: List[TaskScheme] = None


class SPECIAL_EVENT(BaseModel):
    name: str
    description: Optional[str] = None
    date: datetime
    calendar_id: Optional[str]


class DAY(BaseModel):
    # month: int
    day_of_week: str
    special_events: List[SPECIAL_EVENT] = []
    OBJ: BothScheme


class DBJDATA(BaseModel):
    month: int 
    year: int
    data: List[DAY]
