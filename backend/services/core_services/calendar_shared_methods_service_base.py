from typing import Dict

from services import CoreServiceBase

from app_types import *
from DTOs.calendar_dtos import *
from utils import map_nearest_range, get_amount_of_month_days

from postgre import Tasks, Events, Users


class CoreServiceBaseSharedMethods(CoreServiceBase):
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

        out_days = [start_date.day]
        loop_range = (end_date - start_date).days + 1

        # TODO
        # IMPORTANT: May produce duplicate days, if range consists of more than one month!
        # But with current logic, this will work as expected
        for i in range(loop_range):
            if start_date.day + i > curr_month_days:
                out_days.append(i)
            else:
                out_days.append(start_date.day + i)

        objects_by_days: Dict[int, BothScheme] = dict(
            list((day, BothScheme()) for day in out_days)
        )

        for object in objects:
            day_objects = objects_by_days[object.start_date.day]
            if isinstance(object, Events):
                day_objects.events.append(
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
                day_objects.tasks.append(
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

            objects_by_days[object.start_date.day] = day_objects

        return ObjectsRangeData(
            month=curr_datetime.month,
            year=curr_datetime.year,
            data=[
                DayScheme(
                    day_of_week_readable=self.map_weekdays_to_readable(
                        datetime(
                            year=curr_datetime.year,
                            month=curr_datetime.month,
                            day=month_day,
                        ).weekday()
                    ),
                    month_day=month_day,
                    special_events=[],
                    objects=objects,
                )
                for month_day, objects in objects_by_days.items()
            ],
        )
