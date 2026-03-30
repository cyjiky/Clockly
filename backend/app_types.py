from typing import Literal
from enum import Enum, unique

type AppRunningMode = Literal["prod", "test"]
type TypeJWT = Literal["access", "refresh"]


"""
All Enums contain user-readable URL friendly values,
this allows to use these Enums in endpoint PATH parameters
"""


class TimeLineEnum(Enum):
    DAY = "day"
    THREE_DAYS = "three-days"
    WEEK = "week"
    MONTH = "month"


@unique
class VisualizationTimeLineEnum(Enum):
    DAY = "day"
    CURRENT_WEEK = "week"
    MONTH = "month"


@unique
class HeatMapTimeLineEnum(Enum):
    MONTH = "month"
    YEAR = "year"


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
    TASK = "Task"
    EVENT = "Event"


@unique
class UserStatusEnum(Enum):
    USER_REGISTERED = "USER_REGISTERED"
    USER_LOGGED_IN = "USER_LOGGED_IN"
    USER_LOGGED_OUT = "USER_LOGGED_OUT"


@unique
class TaskActionEnum(Enum):
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"


@unique
class DeletionOptions(Enum):
    CASCADE = "cascade"
    SET_NULL = "set-null"
