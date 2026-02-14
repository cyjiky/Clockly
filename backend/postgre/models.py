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
    username: Mapped[str] = mapped_column(String(34))
    email: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    password_hash = Mapped[str]

    def __repr__(self) -> str:
        return f'User:{self.id=}:{self.username=}'


class Tasks(Base): # - названия заметок 
    __tablename__ = "task"

    id = mapped_column(Integer, primary_key=True)
    task_name: Mapped[str]
    additional_description: Mapped[Optional[str]]
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    name_fk: Mapped[int] = mapped_column(ForeignKey('event.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    tasks: Mapped[List["Events"]] = relationship(back_populates="events")

    def __repr__(self) -> str:
        return f'Tasks:{self.id=}:{self.task_name=}'    


class Events(Base): # - задачи (к заметкам дополнительно)
    __tablename__ = "event"

    id = mapped_column(Integer, primary_key=True)
    event_name: Mapped[str]
    additional_description: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    events: Mapped["Tasks"] = relationship(back_populates="tasks")

    def __repr__(self) -> str:
        return f'Events:{self.id=}:{self.event_name=}'
    
