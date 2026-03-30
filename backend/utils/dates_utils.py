from datetime import datetime, timedelta
import calendar
from typing import Tuple
from app_types import ExtendedTimeLineEnum

StartDate = datetime
EndDate = datetime


def get_amount_of_month_days(year: int, month: int) -> int:
    return calendar.monthrange(year, month)[1]


def map_nearest_range(
    date: datetime, timerange: ExtendedTimeLineEnum
) -> Tuple[StartDate, EndDate]:
    match timerange:
        case ExtendedTimeLineEnum.DAY:
            return datetime.combine(
                date.date(), datetime.min.time()
            ), datetime.combine((date).date(), datetime.max.time())

        case ExtendedTimeLineEnum.THREE_DAYS:
            return datetime.combine(
                date.date(), datetime.min.time()
            ), datetime.combine(
                (date + timedelta(days=2)).date(), datetime.max.time()
            )

        case ExtendedTimeLineEnum.WEEK:
            start_week_day = date.weekday()
            start_week_date = date - timedelta(
                days=start_week_day
            )  # Nearest Monday

            end_week_date = start_week_date + timedelta(
                days=6
            )  # Nearest Sunday

            return datetime.combine(
                start_week_date.date(), datetime.min.time()
            ), datetime.combine(end_week_date.date(), datetime.max.time())

        case ExtendedTimeLineEnum.MONTH:
            curr_year = date.year
            curr_month = date.month

            month_n_days = get_amount_of_month_days(curr_year, curr_month)

            return datetime(year=curr_year, month=curr_month, day=1), datetime(
                year=curr_year, month=curr_month, day=month_n_days
            )

        case ExtendedTimeLineEnum.YEAR:
            curr_year = date.year

            return datetime(year=curr_year, month=1, day=1), datetime(year=2027, month=12, day=31)
