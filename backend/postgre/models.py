from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from typing import List, Optional

from sqlalchemy import ForeignKey, func, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(34))
    email: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    password_hash = Mapped[str]

    birthday: Mapped[datetime | None] = mapped_column(default=None)

    tasks: Mapped[List[Tasks]] = relationship("Tasks")
    events: Mapped[List[Events]] = relationship("Events")
    calendars: Mapped[List[Calendars]] = relationship("Calendars")

    def __repr__(self) -> str:
        return f"User:{self.user_id=}:{self.username=}"


class Tasks(Base):  # - названия заметок
    __tablename__ = "tasks"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    additional_description: Mapped[Optional[str]]
    start_date: Mapped[datetime] = mapped_column()
    end_date: Mapped[datetime] = mapped_column()

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.user_id", ondelete="CASCADE")
    )
    calendar_id: Mapped[str | None] = mapped_column(
        ForeignKey("calendars.calendar_id", ondelete="SET NULL")
    )
    calendar: Mapped[Calendars | None] = relationship(
        "Calendars", back_populates="tasks", lazy="selectin"
    )

    completed: Mapped[bool] = mapped_column(default=False)

    def __repr__(self) -> str:
        return f"Task:{self.id}:{self.name}"


class Events(Base):  # - задачи (к заметкам дополнительно)
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    additional_description: Mapped[Optional[str]]
    start_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    end_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    compatibility: Mapped[bool] = mapped_column(default=True)

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.user_id", ondelete="CASCADE")
    )
    calendar_id: Mapped[str | None] = mapped_column(
        ForeignKey("calendars.calendar_id", ondelete="SET NULL")
    )
    calendar: Mapped[Calendars | None] = relationship(
        "Calendars", back_populates="events", lazy="selectin"
    )

    def __repr__(self) -> str:
        return f"Event:{self.id}:{self.name}"


class Calendars(Base):
    __tablename__ = "calendars"

    calendar_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    color: Mapped[str]

    # Must be setted to True only in registration case
    # If is_initial set to True, this calendar shouldn't be deleted
    is_initial: Mapped[bool] = mapped_column(default=False)

    scoring: Mapped[bool] = mapped_column()

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.user_id", ondelete="CASCADE")
    )

    events: Mapped[List["Events"]] = relationship(
        "Events", back_populates="calendar"
    )
    tasks: Mapped[List["Tasks"]] = relationship(
        "Tasks", back_populates="calendar"
    )
