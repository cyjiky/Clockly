from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass 

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(34))
    email: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    password_hash = Mapped[str]

    tasks: Mapped[List[Tasks]] = relationship()
    events: Mapped[List[Events]] = relationship()
    calendars: Mapped[List[Calendars]] = relationship()

    def __repr__(self) -> str:
        return f'User:{self.id=}:{self.username=}'


class Tasks(Base): # - названия заметок 
    __tablename__ = "tasks"

    task_id: Mapped[str] = mapped_column(primary_key=True)
    task_name: Mapped[str]
    additional_description: Mapped[Optional[str]]
    start_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    end_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    user_id: Mapped[str] = mapped_column(ForeignKey('users.user_id'))
    calendar_id: Mapped[str] = mapped_column(ForeignKey("calendars.calendar_id"))
    
    def __repr__(self) -> str:
        return f'Tasks:{self.id}:{self.task_name}'    


class Events(Base): # - задачи (к заметкам дополнительно)
    __tablename__ = "events"

    event_id: Mapped[str] = mapped_column(primary_key=True)
    event_name: Mapped[str]
    additional_description: Mapped[str]
    start_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    end_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    user_id: Mapped[str] = mapped_column(ForeignKey('users.user_id'))
    calendar_id: Mapped[str] = mapped_column(ForeignKey("calendars.calendar_id"))

    def __repr__(self) -> str:
        return f'Events:{self.id}:{self.event_name}'
    
class Calendars(Base):
    __tablename__ = "calendars"

    calendar_id: Mapped[str] = mapped_column(primary_key=True)
    calendar_name: Mapped[str]
    color: Mapped[str]

    # Must be setted to True only in registration case
    # If is_initial set to True, this calendar shouldn't be deleted
    is_initial: Mapped[bool] = mapped_column(default=False)
    
    events: Mapped[List[Events]] = relationship()
    tasks = Mapped[List[Tasks]] = relationship()