from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from postgre.models import *
from app_types import BothTaskEventEnum, TimeLineEnum
from datetime import datetime, time
from utils import map_nearest_range

from typing import TypeVar, List

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

    async def get_tasks_by_userId(self, user_id: str, n: int) -> Tasks | None:
        res = await self.__sesion.execute(
            select(Tasks).where(Tasks.user_id == user_id).limit(n)
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

    async def get_task_by_data(
        self, user_id: str, _data: datetime
    ) -> List[Tasks]:
        if isinstance(_data, datetime):
            _data = _data.date()

        start_day = datetime.combine(_data, time.min)  # 00:00
        end_day = datetime.combine(_data, time.max)  # 23:59

        res = await self.__sesion.execute(
            select(Tasks).where(
                Tasks.user_id == user_id,
                Tasks.start_date >= start_day,
                Tasks.start_date <= end_day,
            )
        )
        return res.scalars().all()

    async def get_event_by_data(
        self, user_id: str, _data: datetime
    ) -> List[Events]:
        if isinstance(_data, datetime):
            _data = _data.date()

        start_day = datetime.combine(_data, time.min)  # 00:00
        end_day = datetime.combine(_data, time.max)  # 23:59

        res = await self.__sesion.execute(
            select(Events).where(
                Events.user_id == user_id,
                Events.start_date >= start_day,
                Events.start_date <= end_day,
            )
        )
        return res.scalars().all()

    async def get_user_initial_calendar(self, user_id: str) -> Calendars:
        res = await self.__sesion.execute(
            select(Calendars).where(
                Calendars.user_id == user_id, Calendars.is_initial == True
            )
        )

        return res.scalars().one_or_none()

    async def get_user_calendars(self, user_id: str) -> List[Calendars]:
        res = await self.__sesion.execute(
            select(Calendars)
            .where(Calendars.user_id == user_id)
        )

        return res.scalars().all()

    async def get_user_calendar_by_name(self, user_id: str, calendar_name: str) -> Calendars | None:
        res = await self.__sesion.execute(
            select(Calendars)
            .where(Calendars.user_id == user_id, Calendars.name == calendar_name)
        )

        return res.scalars().one_or_none()

    async def get_time_objects_by_range(
        self, user_id: str, start_date: datetime, end_date: datetime
    ) -> List[Events | Tasks]:

        stmt1 = select(Events).where(
            Events.user_id == user_id,
            Events.start_date > start_date,
            Events.start_date < end_date,
        )

        stmt2 = select(Tasks).where(
            Tasks.user_id == user_id,
            Tasks.start_date > start_date,
            Tasks.start_date < end_date,
        )

        result_events = (await self.__sesion.execute(stmt1)).scalars().all()
        result_tasks = (await self.__sesion.execute(stmt2)).scalars().all()

        return result_events + result_tasks

    async def delete_tasks(self, task_id) -> None:
        await self.__sesion.execute(
            delete(Tasks).where(Tasks.id == task_id)
        )

    async def delete_events(self, event_id) -> None:
        await self.__sesion.execute(
            delete(Events).where(Events.id == event_id)
        )


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
