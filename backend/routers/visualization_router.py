from fastapi import FastAPI
from fastapi import APIRouter

from DTOs import (
    LineChartScheme,
    LineChartTasksScheme,
    PieChartTasksScheme,
    LineChartEventsScheme,
    PieChartEventsScheme,
    HeatMapScheme
)

chart = APIRouter()


# @chart.get("/task/by_category/{id}") # Pie Chart
# def category_task():
#     pass 

# @chart.get("/task/load_trend/{id}") # Line Chart
# def trend_task(period: str = "week"):
#     pass 

# Event
@chart.get("/event/summary/{id}")
def summary_event(start_time: str, end_time:str):
    pass 

# @chart.get("/event/by_category/{id}") # Pie Chart
# def category_event():
#     pass 

# @chart.get("/event/load_trend/{id}") # Line Chart
# def trend_event(period: str = "week"):
#     pass 

@chart.get("/event/heatmap/{id}") # activity maps
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