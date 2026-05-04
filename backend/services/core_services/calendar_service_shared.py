from typing import Dict, Tuple

from services import CoreServiceBase

from app_types import *
from DTOs.calendar_dtos import *
from utils import map_nearest_range, get_amount_of_month_days
from datetime import datetime, timedelta


from postgre import Tasks, Events, Users


class CoreServiceBaseSharedMethods(CoreServiceBase):
    @staticmethod
    def _append_correct_time_object(objects: BothScheme, object: Events | Tasks) -> None:
            if isinstance(object, Events):
                objects.events.append(
                    EventSchemeOut(
                        name=object.name,
                        description=object.additional_description,
                        start_date=object.start_date,
                        end_date=object.end_date,
                        calendar=(
                            CalendarScheme.model_validate(
                                object.calendar, from_attributes=True
                            )
                            if object.calendar
                            else None
                        ),
                    )
                )
            else:
                objects.tasks.append(
                    TaskSchemeOut(
                        name=object.name,
                        description=object.additional_description,
                        start_date=object.start_date,
                        end_date=object.end_date,
                        calendar=(
                            CalendarScheme.model_validate(
                                object.calendar, from_attributes=True
                            )
                            if object.calendar
                            else None
                        ),
                        completed=object.completed,
                    )
                )

    async def get_data_by_range(
        self,
        user_id: str,
        year: int,
        month: int,
        day: int,
        data_range: ExtendedTimeLineEnum,
    ) -> ObjectsRangeData:

        curr_datetime = datetime(year=year, month=month, day=day)

        start_date, end_date = map_nearest_range(
            date=curr_datetime, timerange=data_range
        )

        objects = await self._PostgreService.get_time_objects_by_range(
            user_id=user_id, start_date=start_date, end_date=end_date
        )

        curr_month_days = get_amount_of_month_days(year=year, month=month)

        # Tuple[int, int] -> year, month, day
        out_days: List[Tuple[int, int, int]] = [(start_date.year, start_date.month, start_date.day)]
        loop_range = (end_date - start_date).days + 1

        # TODO
        # IMPORTANT: May produce duplicate days, if range consists of more than one month!
        # But with current logic, this will work as expected
        next_month_day = 1
        for i in range(loop_range):
            if start_date.day + i > curr_month_days:
                out_days.append((start_date.year, start_date.month+1, next_month_day))
                next_month_day += 1
            else:
                out_days.append((start_date.year, start_date.month, start_date.day + i))

        # Tuple[int, int] -> year, month, day
        objects_by_days: Dict[Tuple[int, int, int], BothScheme] = dict(
            list((month_and_day, BothScheme()) for month_and_day in out_days)
        )

        # Tuple[int, int] -> year, month, day
        _2_digit_days_in_range: List[Tuple[int, int, int]] = []

        while start_date <= end_date:
            _2_digit_days_in_range.append((start_date.year, start_date.month, start_date.day))
            start_date += timedelta(days=1)

        for object in objects:
            if object.full_day:

                # range intersection
                actual_start = max(object.start_date, start_date)
                actual_end = min(object.end_date, end_date)

                for date_tuple in _2_digit_days_in_range:
                    if actual_start <= datetime(year=date_tuple[0], month=date_tuple[1], day=date_tuple[2]) <= actual_end:
                        day_object = objects_by_days.get(date_tuple)

                    self._append_correct_time_object(day_object, object)

            else:
                object_start_date = object.start_date
                day_object = objects_by_days.get((object_start_date.year, object_start_date.month, object_start_date.day))
                self._append_correct_time_object(day_object, object)

        return ObjectsRangeData(
            month=curr_datetime.month,
            year=curr_datetime.year,
            data=[
                DayScheme(
                    day_of_week_readable=self.map_weekdays_to_readable(
                        datetime(
                            year=date_tuple[0],
                            month=date_tuple[1],
                            day=date_tuple[2],
                        ).weekday()
                    ),
                    month_day=date_tuple[2],
                    special_events=[],
                    objects=objects,
                )
                for date_tuple, objects in objects_by_days.items()
            ],
        )
