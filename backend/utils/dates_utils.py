from datetime import datetime, timedelta
import calendar
from typing import Tuple
from app_types import TimeLineEnum

StartDate = datetime
EndDate = datetime


def get_amount_of_month_days(year: int, month: int) -> int:
    return calendar.monthrange(year, month)[1]


def map_nearest_range(
    start_date: datetime, timerange: TimeLineEnum
) -> Tuple[StartDate, EndDate]:
    match timerange:
        case TimeLineEnum.DAY:
            return datetime.combine(start_date.date(), datetime.min.time()), datetime.combine((start_date + timedelta(days=1)).date(), datetime.min.time())

        case TimeLineEnum.THREE_DAYS:
            return datetime.combine(start_date.date(), datetime.min.time()), datetime.combine(
                (start_date + timedelta(days=3)).date(), datetime.min.time()
            )

        case TimeLineEnum.WEEK:
            start_week_day = start_date.weekday()
            start_week_date = start_date - timedelta(
                days=start_week_day
            )  # Nearest Monday

            # Adding 7 days instead of 6 (because weekdays are 0 indexed), because end_date isn't inclusive
            end_week_date = start_week_date + timedelta(
                days=7
            )  # Nearest Sunday

            return datetime.combine(
                start_week_date.date(), datetime.min.time()
            ), datetime.combine(end_week_date.date(), datetime.min.time())

        case TimeLineEnum.MONTH:
            curr_year = start_date.year
            curr_month = start_date.month

            month_n_days = get_amount_of_month_days(curr_year, curr_month)

            return datetime(year=curr_year, month=curr_month, day=1), datetime(year=curr_year, month=curr_month, day=month_n_days)
            
