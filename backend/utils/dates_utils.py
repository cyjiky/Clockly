import datetime
import calendar

from app_types import TimeLineEnum

def map_nearest_range(curr_date: datetime._Date, range: TimeLineEnum) -> datetime:
    match range:
        case TimeLineEnum.DAY:
            return curr_date + datetime.timedelta(days=TimeLineEnum.DAY.value)
        case TimeLineEnum.THREE_DAYS:
            return curr_date + datetime.timedelta(days=TimeLineEnum.THREE_DAYS.value)
        case TimeLineEnum.WEEK:
            return curr_date + datetime.timedelta(days=TimeLineEnum.WEEK.value)
        case TimeLineEnum.MONTH:
            curr_year = curr_date.year
            curr_month = curr_date.month
            curr_days_passed = curr_date.day
            n_days = calendar.monthrange(curr_year, curr_month)
            
            return curr_date + datetime.timedelta(days=n_days-curr_days_passed)