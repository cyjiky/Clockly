from datetime import datetime, timedelta, timezone
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

    match timerange.value:
        case ExtendedTimeLineEnum.DAY.value:
            return datetime.combine(
                date.date(), datetime.min.time(), tzinfo=timezone.utc
            ), datetime.combine(
                (date).date(), datetime.max.time(), tzinfo=timezone.utc
            )

        case ExtendedTimeLineEnum.THREE_DAYS.value:
            return datetime.combine(
                date.date(), datetime.min.time(), tzinfo=timezone.utc
            ), datetime.combine(
                (date + timedelta(days=2)).date(),
                datetime.max.time(),
                tzinfo=timezone.utc,
            )

        case ExtendedTimeLineEnum.WEEK.value:
            start_week_day = date.weekday()
            start_week_date = date - timedelta(
                days=start_week_day
            )  # Nearest Monday

            end_week_date = start_week_date + timedelta(
                days=6
            )  # Nearest Sunday

            return datetime.combine(
                start_week_date.date(),
                datetime.min.time(),
                tzinfo=timezone.utc,
            ), datetime.combine(
                end_week_date.date(), datetime.max.time(), tzinfo=timezone.utc
            )

        case ExtendedTimeLineEnum.MONTH.value:
            curr_year = date.year
            curr_month = date.month

            month_n_days = get_amount_of_month_days(curr_year, curr_month)

            return datetime(
                year=curr_year, month=curr_month, day=1, tzinfo=timezone.utc
            ), datetime(
                year=curr_year,
                month=curr_month,
                day=month_n_days,
                tzinfo=timezone.utc,
            )

        case ExtendedTimeLineEnum.YEAR.value:
            curr_year = date.year

            return datetime(
                year=curr_year, month=1, day=1, tzinfo=timezone.utc
            ), datetime(year=2027, month=12, day=31, tzinfo=timezone.utc)
