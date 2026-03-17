from typing import Literal
from enum import Enum, unique

type AppRunningMode = Literal["prod", "test"]
type TypeJWT = Literal["access", "refresh"]

import typing
import datetime

@unique
class TimeLineEnum(Enum):
    DAY = datetime.timedelta(days=1)
    THREE_DAYS = datetime.timedelta(days=3)
    WEEK = datetime.timedelta(weeks=1)
    
    # We need to manually calculate end of current month
    # Because amount of days in months can range from 28 up to 31
    MONTH = None

@unique
class EventEnum(Enum):
    TASK_CREATED = "TASK_CREATED"
    TASK_UPDATED = "TASK_UPDATED"
    TASK_DELETED = "TASK_DELETED"


@unique
class TaskEnum(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    ARCHIVED = "ARCHIVED"


class BothTaskEventEnum(Enum):
    TASK = "TASK"
    EVENT = "EVENT"
    BOTH = "BOTH"

class TimeObjectsEnum(Enum):
    TASK = "TASK"
    EVENT = "EVENT"

@unique
class UserStatusEnum(Enum):
    USER_REGISTERED = "USER_REGISTERED"
    USER_LOGGED_IN = "USER_LOGGED_IN"
    USER_LOGGED_OUT = "USER_LOGGED_OUT"

@unique
class TaskActionEnum(Enum):
    COMPLETE = "COMPLETE_TASK"
    INCOMPLETE = "INCOMPLITE_TASK"