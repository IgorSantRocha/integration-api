from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class StnBaseSC(BaseModel):
    chamado: str
    status: str


class StnBaseCreateSC(StnBaseSC):
    projeto: str
    num_ref_operador_logistico: str
    contratante: str
    cod_cliente: str
    grupo_cliente: str
    nome_cliente: str
    cnpj_cpf: str
    fone: str
    grupo_servico: str
    servico: str
    serial_instalado: str
    tipo_equipamento_instalado: str
    modelo_instalado: str
    serial_retirado: str
    tipo_equipamento_retirado: str
    modelo_retirado: str
    partes_e_pecas: str
    operador_logistico: str
    prestador: str
    tecnico: str
    estado: str
    cidade: str
    regiao: str
    endereco: str
    complemento: str
    bairro: str
    cep: str
    numero: str
    id_do_equipamento: str
    tipo_do_equipamento: str
    observacões_atendimento: str
    observacões: str
    descricao_motivo: str
    descricao_motivo_1ª_visita: str
    descricao_motivo_2ª_visita: str
    defeito: str
    solucao: str
    remarks: str
    tipo_pessoa: str
    origem_da_venda: str
    vendedor: str
    criado_por: str
    ultima_modificacao: str
    numero_de_visitas: int
    data_primeira_visita: str
    data_segunda_visita: str
    data_de_reabertura_1: str
    data_de_reabertura_2: str
    abono: str
    kit: str
    quantidade_de_kits: int
    aberta_por_integracao: str
    baixa_mobile: str
    foto_assinatura: str
    classe: str
    nome_da_causa: str
    os_emergencial: str
    flag_emergencial_modificado_por: str
    os_the_flash: str
    flag_the_flash_modificado_por: str
    data_abertura: datetime
    data_limite_cliente: datetime
    data_limite: datetime
    data_modificacao: datetime
    data_atendimento: datetime
    data_de_modificacao_da_flag_emergencial: datetime
    data_de_modificacao_da_flag_the_flash: datetime
    status_atual: str
    codtitulo_atualizado_stone: str
    data_retorno_stone: datetime
    dt_importado: datetime


class StnBaseUpdateStatusSC(StnBaseCreateSC):
    antigo_status: str


class StnBaseUpdateSC(StnBaseCreateSC):
    antigo_status: str


class StnBaseInDbBaseSC(StnBaseSC):
    id: int
