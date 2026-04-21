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

chart = APIRouter()


@chart.get("/event/summary/{id}")
def summary_event(start_time: str, end_time: str):
    pass


@chart.get("/event/heatmap/{id}")
def summary_event() -> HeatMapScheme:
    pass


@chart.get("/task/line-chart")
def task_line_chart() -> LineChartScheme[LineChartTasksScheme]:
    pass


@chart.get("/task/pie")
def task_line_chart() -> LineChartScheme[PieChartTasksScheme]:
    pass


@chart.get("/event/line-chart")
def task_line_chart() -> LineChartScheme[LineChartEventsScheme]:
    pass


@chart.get("/event/line-chart")
def task_line_chart() -> LineChartScheme[PieChartEventsScheme]:
    pass
