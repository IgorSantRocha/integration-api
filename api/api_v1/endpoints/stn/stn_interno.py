from typing import Any, List, Dict
import logging

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.stn_controle_schema import StnControleSC
from crud.crud_stn import stn_controle, stn_base_essential
from schemas.stn_controle_schema import StnControleCreateSC, StnControleUpdateStatusDesejadoSC
from schemas.stn_base_schema import StnBaseInDbBaseSC


router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/interno/", response_model=List[StnControleSC],
            description='Lista todos os casos da tabela que ainda não foram enviados',
            status_code=status.HTTP_200_OK,
            )
async def read_chamados(
        db: Session = Depends(get_db)
) -> Any:
    """
    Retrieve controle.
    """
    logger.info("Consultando chamados")
    return stn_controle.get_multi_filter(db=db, filterby='enviado', filter=0)


@router.post("/interno/", response_model=StnControleSC,
             description='Adiciona um chamado específico na tabela de controle',
             status_code=status.HTTP_201_CREATED)
async def adicionar_chamado(
        *,
        db: Session = Depends(get_db),
        controle_in: StnControleCreateSC,
) -> Any:
    """
    Cria uma linha do chamado na tabela de controle
    """
    logger.info("Cria chamado")
    controle = stn_controle.create(db=db, obj_in=controle_in)
    return controle


@router.patch("/interno/",
              description='Muda o status desejado do caso',
              status_code=status.HTTP_201_CREATED,
              response_model=StnControleUpdateStatusDesejadoSC)
async def trocar_status_desejado(
        *,
        db: Session = Depends(get_db),
        controle_in: StnControleUpdateStatusDesejadoSC,
) -> Any:
    """
    Cria uma linha do chamado na tabela de controle
    """
    logger.info("Update status desejado do chamado")
    db_obj = stn_controle.get(db=db, id=controle_in.id)

    if db_obj:
        controle = stn_controle.update_status_desejado(
            db=db, db_obj=db_obj, obj_in=controle_in)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não foi possível encontrar o chamado de id: {controle_in.id}')
    return controle


@router.post("/interno/multi", response_model=Dict[str, Any],
             description='Adiciona uma chamada na tabela de controle',
             status_code=status.HTTP_201_CREATED)
async def adicionar_chamados(
        *,
        db: Session = Depends(get_db),
        controle_in: List[StnControleCreateSC],
) -> Any:
    """
    Insere uma lista de chamados na tabela de controle
    """
    logger.info("Adiciona chamados em massa")
    controle_objs = stn_controle.create_multi(
        db=db, obj_in=controle_in)

    return controle_objs


@router.delete(path="/interno/{id}", response_model=StnControleSC,
               description='Deleta um chamado da tabela de controle',
               status_code=status.HTTP_201_CREATED)
async def delete_chamado(
        *,
        db: Session = Depends(get_db),
        id: int,
) -> Any:
    """
    Deleta um chamadp da lista pelo ID da tabela de controle
    """
    controle = stn_controle.get(db=db, id=id)
    if not controle:
        raise HTTPException(status_code=404, detail="Chamado não encontrado")
    controle = stn_controle.remove(db=db, id=id)
    return controle


@router.get("/interno/teste", response_model=List[StnBaseInDbBaseSC],
            description='Lista todos os casos da tabela que ainda não foram enviados',
            status_code=status.HTTP_200_OK,
            )
async def read_chamados(
        db: Session = Depends(get_db)
) -> Any:
    """
    Retrieve controle.
    """
    logger.info("Consultando chamados")
    return stn_base_essential.get_multi_filter(db=db, filterby='status', filter='NOVA')
