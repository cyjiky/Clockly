from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class ExportJSONOBject(BaseModel):
    object_type: Literal["event", "task"]

    id: str

    name: str
    description: str | None

    start_date: datetime
    end_date: datetime

    full_day: bool

    calendar_id: str | None
    completed: bool | None
