from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update, or_, and_, union
from postgre.models import *
from app_types import BothTaskEventEnum, TimeLineEnum
from datetime import datetime, time
from utils import map_nearest_range

from config import settings

from typing import TypeVar, List, AsyncGenerator

M = TypeVar("M", bound=Base)

class PostgreService:
    def __init__(self, session: AsyncSession):
        self.__sesion = session

    async def commit(self) -> None:
        await self.__sesion.commit()

    async def flush(self) -> None:
        await self.__sesion.flush()

    async def flush_models(self, *models: Base) -> None:
        """Adds *models: Base to the session and flushes them"""
        self.__sesion.add_all(models)
        await self.flush()

    async def create_model(self, Model: M, **kwargs) -> M:
        return Model(**kwargs)

    async def get_user_by_id(self, user_id: str) -> Users | None:
        res = await self.__sesion.execute(
            select(Users).where(Users.user_id == user_id)
        )

        return res.scalars().one_or_none()

    async def get_user_by_username(self, username: str) -> Users | None:
        res = await self.__sesion.execute(
            select(Users).where(Users.username == username)
        )
        return res.scalars().one_or_none()

    async def get_user_by_email(self, email: str) -> Users | None:
        res = await self.__sesion.execute(
            select(Users).where(Users.email == email)
        )
        return res.scalars().one_or_none()

    async def get_tasks_by_userId(self, user_id: str, page: int) -> Tasks | None:
        res = await self.__sesion.execute(
            select(Tasks)
            .where(Tasks.user_id == user_id)
            .order_by(Tasks.start_date.desc())
            .offset(page * settings.pagination)
            .limit(settings.pagination)
        )
        return res.scalars().all()

    async def get_events_by_userId(
        self, user_id: str, n: int
    ) -> Events | None:
        res = await self.__sesion.execute(
            select(Events).where(Events.user_id == user_id).limit(n)
        )
        return res.scalars().all()

    async def get_event_by_id(self, event_id: str) -> Events:
        res = await self.__sesion.execute(
            select(Events).where(Events.id == event_id)
        )
        return res.scalars().one_or_none()

    async def get_task_by_id(self, task_id: str) -> Tasks:
        res = await self.__sesion.execute(
            select(Tasks).where(Tasks.id == task_id)
        )
        return res.scalars().one_or_none()

    # async def get_task_by_data(self, user_id: str, data: datetime) -> Tasks | None:
    #     res = await self.__sesion.execute(
    #         select(Tasks)
    #         .where(
    #             Tasks.user_id == user_id,
    #             cast(Tasks.datetime, Date) == data)
    #     )
    #     return res.scalars().all()

    async def get_time_objects_by_date(
        self, user_id: str, date: datetime, time_objects_type: BothTaskEventEnum
    ) -> List[Tasks | Events]:
        if isinstance(date, datetime):
            date = date.date()

        start_day = datetime.combine(date, time.min)  # 00:00
        end_day = datetime.combine(date, time.max)  # 23:59

        return await self.get_time_objects_by_range(user_id=user_id, start_date=start_day, end_date=end_day)

    # async def get_tasks_by_date(
    #     self, user_id: str, _date: datetime
    # ) -> List[Tasks]:
    #     if isinstance(_date, datetime):
    #         _date = _date.date()

    #     start_day = datetime.combine(_date, time.min)  # 00:00
    #     end_day = datetime.combine(_date, time.max)  # 23:59

    #     res = await self.__sesion.execute(
    #         select(Tasks).where(
    #             Tasks.user_id == user_id,
    #             Tasks.start_date >= start_day,
    #             Tasks.start_date <= end_day,
    #         )
    #     )
    #     return res.scalars().all()

    # async def get_events_by_date(
    #     self, user_id: str, date: datetime
    # ) -> List[Events]:
    #     if isinstance(date, datetime):
    #         date = date.date()

    #     start_day = datetime.combine(date, time.min)  # 00:00
    #     end_day = datetime.combine(date, time.max)  # 23:59

    #     res = await self.__sesion.execute(
    #         select(Events).where(
    #             Events.user_id == user_id,
    #             Events.start_date >= start_day,
    #             Events.start_date <= end_day,
    #         )
    #     )
    #     return res.scalars().all()

    async def get_user_initial_calendar(self, user_id: str) -> Calendars:
        res = await self.__sesion.execute(
            select(Calendars).where(
                Calendars.user_id == user_id, Calendars.is_initial == True
            )
        )

        return res.scalars().one_or_none()

    async def get_user_calendars(self, user_id: str) -> List[Calendars]:
        res = await self.__sesion.execute(
            select(Calendars).where(Calendars.user_id == user_id)
        )

        return res.scalars().all()

    async def get_user_calendar_by_name(
        self, user_id: str, calendar_name: str
    ) -> Calendars | None:
        res = await self.__sesion.execute(
            select(Calendars).where(
                Calendars.user_id == user_id, Calendars.name == calendar_name
            )
        )

        return res.scalars().one_or_none()

    async def get_calendar_by_id(
        self, user_id: str, calendar_id: str
    ) -> Calendars | None:
        res = await self.__sesion.execute(
            select(Calendars).where(
                Calendars.user_id == user_id,
                Calendars.calendar_id == calendar_id,
            )
        )

        return res.scalars().one_or_none()

    async def get_time_objects_by_range(
        self, user_id: str, start_date: datetime, end_date: datetime
    ) -> List[Events | Tasks]:

        # Events query
        event_q = select(Events).where(
            Events.user_id == user_id,
            or_(Events.end_date >= start_date, Events.start_date >= end_date)
        )

        tasks_q = select(Tasks).where(
            Tasks.user_id == user_id,
            or_(Tasks.end_date >= start_date, Tasks.start_date >= end_date)
        )

        result_events = (await self.__sesion.execute(event_q)).scalars().all()
        result_tasks = (await self.__sesion.execute(tasks_q)).scalars().all()

        return result_events + result_tasks

    async def delete_task(self, user_id: str, task_id: str) -> None:
        await self.__sesion.execute(
            delete(Tasks)
            .where(Tasks.id == task_id)
        )

    async def delete_event(self, user_id: str, event_id: str) -> None:
        await self.__sesion.execute(
            delete(Events)
            .where(Events.id == event_id, Events.user_id == user_id)
        )

    async def delete_calendar(self, user_id: str, calendar_id: str) -> None:
        """This function won't delete user's initial calendar"""

        await self.__sesion.execute(
            delete(Calendars)
            .where(
                Calendars.calendar_id == calendar_id,
                Calendars.user_id == user_id,
                Calendars.is_initial == False # Initial calendar must NOT be deleted
            )
        )

    async def delete_calendar_time_objects(self, user_id: str, calendar_id: str) -> None:
        await self.__sesion.execute(
            delete(Events)
            .where(Events.user_id == user_id, Events.calendar_id == calendar_id)
        )

        await self.__sesion.execute(
            delete(Tasks)
            .where(Tasks.user_id == user_id, Tasks.calendar_id == calendar_id)
        )


    async def remove_time_objects_calendar(self, user_id: str, calendar_id: str):
        await self.__sesion.execute(
            update(Events.__table__) # https://stackoverflow.com/questions/2631935/sqlalchemy-a-better-way-for-update-with-declarative
            .where(Events.user_id == user_id, Events.calendar_id == calendar_id)
            .values(calendar_id=None)
        )

        await self.__sesion.execute(
            update(Tasks.__table__)
            .where(Tasks.user_id == user_id, Tasks.calendar_id == calendar_id)
            .values(calendar_id=None)
        )

    async def time_objects_range_generator(self, start_date: datetime, end_date: datetime, user_id: str) -> AsyncGenerator[None, List[Events | Tasks]]:
        events_stmt = (
            select(Events)
            .where(Events.user_id == user_id, Events.start_date <= end_date, Events.end_date <= start_date)
        ).execution_options(yield_per=100)

        tasks_stmt = (
            select(Events)
            .where(Events.user_id == user_id, Events.start_date <= end_date, Events.end_date <= start_date)
        ).execution_options(yield_per=100)

        full_stmt = union(events_stmt, tasks_stmt)

        async with self.__sesion.stream_scalars(full_stmt) as result:
            async for scalars in result:
                yield scalars


# Юзера по его юзернейму
# Все события юзера - все / на сегодня
# Все задания юзера - все / на сегодня
# принимать параметр фильтра

# отдает актуальные события или задания на сегодня


# async def get_user_by_id(self, user_id: str) -> User | None:
#     result = await self.__session.execute(
#         select(User)
#         .options(selectinload(User.followed), selectinload(User.followers))
#         .where(User.user_id == user_id)
#     )
#     return result.scalar()


# async def get_fresh_followedposts(self, user: User, n: int) -> List[Post]:
#     result = await  self.__session.execute(
#         select(Post)
#         .where(Post.owner.in((user.followed)))
#         .order_by(Post.published.desc())
#         .limit(n)
#     )

#     return result.scalars().all()


# async def delete_expired_jwts(db: AsyncSession, UNIX_timestamp: int | float) -> None:
# return await db.execute(
#     delete(JWTTable)
#     .where(JWTTable.expires_at < int(UNIX_timestamp))
# )
