from fastapi import FastAPI
from fastapi import APIRouter

chart = APIRouter()

# Tasks
@chart.get("/task/summary/{id}")
def summary_task(start_time: str, end_time:str):
    pass 

@chart.get("/task/by_category/{id}") # Pie Chart
def category_task():
    pass 

@chart.get("/task/load_trend/{id}") # Line Chart
def trend_task(period: str = "week"):
    pass 

@chart.get("/task/heatmap/{id}") # activity maps
def summary_task():
    pass 

# Event
@chart.get("/event/summary/{id}")
def summary_event(start_time: str, end_time:str):
    pass 

@chart.get("/event/by_category/{id}") # Pie Chart
def category_event():
    pass 

@chart.get("/event/load_trend/{id}") # Line Chart
def trend_event(period: str = "week"):
    pass 

@chart.get("/event/heatmap/{id}") # activity maps
def summary_event():
    pass 