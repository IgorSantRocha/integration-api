from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class StnControleBaseSC(BaseModel):
    chamado_id: int
    status_desejado: str


class StnControleCreateSC(StnControleBaseSC):
    pass


class StnControleUpdateStatusDesejadoSC(StnControleBaseSC):
    pass


class StnControleUpdateSC(StnControleBaseSC):
    enviado: bool
    msg_resposta: str
    statuscode_resposta: int
    atualizadoem: datetime = Field(
        default_factory=datetime.now)


class StnControleInDbBaseSC(StnControleBaseSC):
    id: int


class StnControleSC(StnControleInDbBaseSC):
    criadoem: datetime
    enviado: bool
    msg_resposta: Optional[str]
    statuscode_resposta: Optional[int]
