from typing import Literal
from enum import Enum, unique

type AppRunningMode = Literal["prod", "test"]
type TypeJWT = Literal["access", "refresh"]

import typing
from datetime import timedelta


@unique
class TimeLineEnum(Enum):
    DAY = "DAY"
    THREE_DAYS = "THREE_DAYS"
    WEEK = "WEEK"
    MONTH = "MONTH"


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


@unique
class BothTaskEventEnum(Enum):
    TASK = "TASK"
    EVENT = "EVENT"
    BOTH = "BOTH"


@unique
class TimeObjectsEnum(Enum):
    "Contains user-readable values"

    TASK = "Task"
    EVENT = "Event"


@unique
class UserStatusEnum(Enum):
    USER_REGISTERED = "USER_REGISTERED"
    USER_LOGGED_IN = "USER_LOGGED_IN"
    USER_LOGGED_OUT = "USER_LOGGED_OUT"


@unique
class TaskActionEnum(Enum):
    COMPLETE = "COMPLETE_TASK"
    INCOMPLETE = "INCOMPLITE_TASK"
