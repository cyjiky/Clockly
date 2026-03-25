import datetime
import calendar
from typing import Tuple
from app_types import TimeLineEnum

StartDate = datetime.datetime
EndDate = datetime.datetime

def get_amount_of_month_days(year: int, month: int) -> int:
    return calendar.monthrange(year, month)[1]

def map_nearest_range(
    start_date: datetime.datetime, timerange: TimeLineEnum
) -> Tuple[StartDate, EndDate]:
    match timerange:
        case TimeLineEnum.DAY:
            return start_date, start_date + datetime.timedelta(
                days=1
            )
        case TimeLineEnum.THREE_DAYS:
            return start_date, start_date + datetime.timedelta(
                days=3
            )
        case TimeLineEnum.WEEK:
            return start_date, start_date + datetime.timedelta(
                days=7
            )
        case TimeLineEnum.MONTH:
            curr_year = start_date.year
            curr_month = start_date.month
            curr_days_passed = start_date.day
            n_days = get_amount_of_month_days(curr_year, curr_month)

            return datetime.datetime(
                year=start_date.year, month=start_date.month, day=1
            ), start_date + datetime.timedelta(
                days=n_days - curr_days_passed
            )
