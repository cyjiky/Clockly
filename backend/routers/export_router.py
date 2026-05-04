from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from sqlalchemy.ext.asyncio import AsyncSession

from services import *
from postgre import get_session_depends, Users, merge_model
from auth.auth_utils import authorize_private_endpoint

export = APIRouter()


@export.get("/export/csv")
async def csv_export_data(
    start_data: datetime,
    end_date: datetime,
    postgres_session: AsyncSession = Depends(get_session_depends),
    user_: Users = Depends(authorize_private_endpoint)
):
    service = await ExportService.create(postgres_session)
    user = await merge_model(user_, postgres_session)

    return StreamingResponse(
        service.csv_historic_data_generator(user.user_id, start_data, end_date),
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=historic_data.csv"
        },
    )


@export.get("/export/json")
async def json_export_data(
    start_data: datetime,
    end_date: datetime,
    postgres_session: AsyncSession = Depends(get_session_depends),
    user_: Users = Depends(authorize_private_endpoint)
):
    service = await ExportService.create(postgres_session)
    user = await merge_model(user_, postgres_session)

    return StreamingResponse(
        service.json_historic_data_generator(user.user_id, start_data, end_date),
        media_type="application/json",
        headers={
            "Content-Disposition": "attachment; filename=historic_data.json"
        },
    )
