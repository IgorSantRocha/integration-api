from typing import Any, List
import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.request import RequestClient
from schemas.stn_controle_schema import StnControleSC
from api.deps import get_db
from crud.crud_stn import stn_controle
from schemas.stn_controle_schema import StnControleCreateSC, StnControleUpdateSC


router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", response_model=List[StnControleSC])
async def read_chamados(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    Retrieve controle.
    """
    logger.info("Consultando carros")
    return stn_controle.get_multi(db=db, skip=skip, limit=limit)


@router.post("/add_chamado", response_model=StnControleSC)
async def adicionar_chamado(
        *,
        db: Session = Depends(get_db),
        controle_in: StnControleCreateSC,
) -> Any:
    """
    Create new line in control.
    """
    controle = stn_controle.create(db=db, obj_in=controle_in)
    return controle


@router.post("/add_chamados", response_model=list[StnControleSC])
async def adicionar_chamados(
        *,
        db: Session = Depends(get_db),
        controle_in: list[StnControleCreateSC],
) -> Any:
    """
    Create new lines in control.
    """
    controle_objs: list[StnControleSC] = stn_controle.create_multi(
        db=db, obj_in=controle_in)

    return controle_objs


@router.delete(path="/{id}", response_model=StnControleSC)
async def delete_chamado(
        *,
        db: Session = Depends(get_db),
        id: int,
) -> Any:
    """
    Delete an item.
    """
    controle = stn_controle.get(db=db, id=id)
    if not controle:
        raise HTTPException(status_code=404, detail="Chamado não encontrado")
    controle = stn_controle.remove(db=db, id=id)
    return controle


@router.get(path="/request")
async def request():
    client = RequestClient('GET', 'https://viacep.com.br/ws/03073010/json/',
                           {'test': 'test'}, {'param1': 'teste'}, 30)
    response = await client.send_api_request()
    return response
