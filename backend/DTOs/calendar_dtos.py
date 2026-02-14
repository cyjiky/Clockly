from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Task(BaseModel):
    name: str
    description: Optional[str] = None
    start_time: str
    end_time: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class Event(BaseModel):
    name: str
    description: Optional[str] = None
    start_time: str
    end_time: str
    start_date: datetime
    end_date: Optional[datetime] = None
    calendar_id: str
    calendar_name: str 
    repeat_days: List[str] = [] 
    repeat_time: List[datetime] = [] 