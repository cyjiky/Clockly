from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from services import *

export = APIRouter()


@export.get("/export/csv")
async def csv_export_data(start_data: datetime, end_date: datetime):
    service = ExportService()

    return StreamingResponse(
        service.csv_historic_data_generator(start_data, end_date),
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=historic_data.csv"
        },
    )


@export.get("/export/json")
async def json_export_data(start_data: datetime, end_date: datetime):
    service = ExportService()

    return StreamingResponse(
        service.json_historic_data_generator(start_data, end_date),
        media_type="application/json",
        headers={
            "Content-Disposition": "attachment; filename=historic_data.json"
        },
    )
