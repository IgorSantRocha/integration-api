
import logging
from fastapi import APIRouter

from core.request import StnHomologRequestClient


router = APIRouter()
logger = logging.getLogger(__name__)


@router.get(path="/requests/consulta")
async def get_service_orders(id: int = None, status: str = 'NOVA', current_page: int = 1):
    parameters = dict(
        id=id,
        status=status,
        current_page=current_page
    )

    client = StnHomologRequestClient(
        method='get',
        request_data=parameters
    )
    response = await client.send_api_request()
    return response
