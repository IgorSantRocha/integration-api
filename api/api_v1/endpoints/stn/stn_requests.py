
import logging
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from core.request import StnHomologRequestClient
from schemas.request_body_schema import StnAlterSC, StnSucessoSC


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


@router.patch(path="/requests/consulta/{chamado}",
              response_model=StnSucessoSC,
              status_code=status.HTTP_202_ACCEPTED)
async def patch_service_orders(
    chamado: str,
    parameters: StnAlterSC,
):
    parameters = jsonable_encoder(parameters)
    client = StnHomologRequestClient(
        method='patch',
        request_data=parameters,
        chamado=chamado
    )
    response = await client.send_api_request()
    return response
