from fastapi import FastAPI
from fastapi import APIRouter

from DTOs import (
    LineChartScheme,
    LineChartTasksScheme,
    PieChartTasksScheme,
    LineChartEventsScheme,
    PieChartEventsScheme,
    HeatMapScheme,
)

from exceptions_handler import endpoint_exception_logger

chart = APIRouter()


@chart.get("/event/summary/{id}")
@endpoint_exception_logger
def summary_event(start_time: str, end_time: str):
    pass


@chart.get("/event/heatmap/{id}")
@endpoint_exception_logger
def summary_event() -> HeatMapScheme:
    pass


@chart.get("/task/line-chart")
@endpoint_exception_logger
def task_line_chart() -> LineChartScheme[LineChartTasksScheme]:
    pass


@chart.get("/task/pie")
@endpoint_exception_logger
def task_line_chart() -> LineChartScheme[PieChartTasksScheme]:
    pass


@chart.get("/event/line-chart")
@endpoint_exception_logger
def task_line_chart() -> LineChartScheme[LineChartEventsScheme]:
    pass


@chart.get("/event/line-chart")
@endpoint_exception_logger
def task_line_chart() -> LineChartScheme[PieChartEventsScheme]:
    pass
