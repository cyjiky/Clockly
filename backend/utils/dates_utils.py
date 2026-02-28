import datetime
import calendar
from typing import Tuple
from app_types import TimeLineEnum

StartDate = datetime.datetime
EndDate = datetime.datetime


def map_nearest_range(
    curr_date: datetime.datetime, timerange: TimeLineEnum
) -> Tuple[StartDate, EndDate]:
    match timerange:
        case TimeLineEnum.DAY:
            return curr_date, curr_date + datetime.timedelta(
                days=TimeLineEnum.DAY.value
            )
        case TimeLineEnum.THREE_DAYS:
            return curr_date, curr_date + datetime.timedelta(
                days=TimeLineEnum.THREE_DAYS.value
            )
        case TimeLineEnum.WEEK:
            return curr_date, curr_date + datetime.timedelta(
                days=TimeLineEnum.WEEK.value
            )
        case TimeLineEnum.MONTH:
            curr_year = curr_date.year
            curr_month = curr_date.month
            curr_days_passed = curr_date.day
            n_days = calendar.monthrange(curr_year, curr_month)

            return datetime.datetime(
                year=curr_date.year, month=curr_date.month, day=1
            ), curr_date.date + datetime.timedelta(
                days=n_days - curr_days_passed
            )
