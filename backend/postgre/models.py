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

    id = mapped_column(Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(34))
    email: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    password_hash = Mapped[str]

    tasks: Mapped[List[Tasks]] = relationship()
    events: Mapped[List[Events]] = relationship()

    def __repr__(self) -> str:
        return f'User:{self.id=}:{self.username=}'


class Tasks(Base): # - названия заметок 
    __tablename__ = "tasks"

    id = mapped_column(Integer, primary_key=True)
    task_id: Mapped[str] = mapped_column(primary_key=True)
    task_name: Mapped[str]
    additional_description: Mapped[Optional[str]]
    start_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    end_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    user_id: Mapped[str] = mapped_column(ForeignKey('users.user_id'))
    event_id: Mapped[str] = mapped_column(ForeignKey('events.event_id'))

    def __repr__(self) -> str:
        return f'Tasks:{self.id}:{self.task_name}'    


class Events(Base): # - задачи (к заметкам дополнительно)
    __tablename__ = "events"

    id = mapped_column(Integer, primary_key=True)
    event_id: Mapped[str] = mapped_column(primary_key=True)
    event_name: Mapped[str]
    additional_description: Mapped[str]
    start_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    end_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    user_id: Mapped[str] = mapped_column(ForeignKey('users.user_id'))

    tasks: Mapped["Tasks"] = relationship()

    def __repr__(self) -> str:
        return f'Events:{self.id}:{self.event_name}'
    
