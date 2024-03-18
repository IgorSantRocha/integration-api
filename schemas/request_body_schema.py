from pydantic import BaseModel, Field
from datetime import datetime


class StnTecnicoSC(BaseModel):
    nomeTecnico: str = Field(
        default='Igor Santos Rocha')
    numeroDoc: str = Field(
        default='482.000.000-00 (substituir pelo correto)')


class StnAlterSC(BaseModel):
    status: str = Field(
        default='EM CAMPO')
    prestador: str = Field(
        default='C-TRENDS')
    tecnico: StnTecnicoSC
    dataAtendimento: datetime


class StnSucessoSC(BaseModel):
    message: str = Field(
        default='Dados do Chamado Nº 000000 gravados com Sucesso')
