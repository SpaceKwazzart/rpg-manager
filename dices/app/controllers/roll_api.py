from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.services import get_roll_service
from app.schemas import ResponseRollDTO, RequestRollDTO
from app.config import logger

roll_router = APIRouter()


@roll_router.post(
    '/roll/',
    response_model=ResponseRollDTO,
    response_model_exclude_none=True
)
async def roll_dices(
    roll_service=Depends(get_roll_service),
    request_data: RequestRollDTO = Body()
):
    try:
        logger.debug(request_data)
        return await roll_service.roll_dices(request_data)
    except Exception as e:
        logger.error('Strange Exception appeared!')
        logger.error(e)
        raise e
