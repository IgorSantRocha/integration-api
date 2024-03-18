from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class StnControleBaseSC(BaseModel):
    status_desejado: str = Field(json_schema_extra={
        'title': 'Status final desejado',
        'description': 'Passa o status para o qual o status deve ser alterado',
        'examples': ['NOVA', 'RECEBIDA', 'EM CAMPO'],
    })


class StnControleCreateSC(StnControleBaseSC):
    chamado_id: int
    pass


class StnControleUpdateStatusDesejadoSC(StnControleBaseSC):
    id: int
    atualizadoem: datetime = Field(
        default_factory=datetime.now)
    enviado: bool = Field(default_factory=False)


class StnControleUpdateSC(StnControleBaseSC):
    id: int
    enviado: bool = Field(
        default_factory=False)
    msg_resposta: str
    statuscode_resposta: int
    atualizadoem: datetime = Field(
        default_factory=datetime.now)


class StnControleInDbBaseSC(StnControleBaseSC):
    id: int
    chamado_id: int


class StnControleSC(StnControleInDbBaseSC):
    criadoem: datetime = Field(
        default_factory=datetime.now)
    status_desejado: str = Field(json_schema_extra={
        'title': 'Status final desejado',
        'description': 'Passa o status para o qual o status deve ser alterado',
        'examples': ['NOVA', 'RECEBIDA', 'EM CAMPO'],
    })
    enviado: bool = Field(default_factory=False)
    msg_resposta: Optional[str]
    statuscode_resposta: Optional[int]
