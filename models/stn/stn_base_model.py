from sqlalchemy import Column, Integer, String, DateTime, Text

from db.base_class import Base


class StnBaseEssentialModel(Base):
    __tablename__ = 'TB_Stone'
    id = Column("ID", Integer, primary_key=True)
    chamado = Column("Chamado", String(35))
    status = Column("Status", String(20))
    __table_args__ = {'extend_existing': True}


class StnBaseModel(StnBaseEssentialModel):
    __table_args__ = {'extend_existing': True}

    projeto = Column("Projeto", String(20))
    num_ref_operador_logístico = Column(
        "Num# Ref# Operador Logístico", String(20))
    contratante = Column("Contratante", String(20))
    cod_cliente = Column("Cod# Cliente", String(40))
    grupo_cliente = Column("Grupo Cliente", String(20))
    nome_cliente = Column("Nome Cliente", String(70))
    cnpj_cpf = Column("CNPJ / CPF", String(20))
    fone = Column("Fone", String(40))
    grupo_serviço = Column("Grupo Serviço", String(20))
    serviço = Column("Serviço", String(30))
    serial_instalado = Column("Serial Instalado", String(20))
    tipo_equipamento_instalado = Column(
        "Tipo Equipamento Instalado", String(20))
    modelo_instalado = Column("Modelo Instalado", String(20))
    serial_retirado = Column("Serial Retirado", String(50))
    tipo_equipamento_retirado = Column("Tipo Equipamento Retirado", String(20))
    modelo_retirado = Column("Modelo Retirado", String(20))
    partes_e_peças = Column("Partes e Peças", String(20))
    operador_logístico = Column("Operador Logístico", String(10))
    prestador = Column("Prestador", String(20))
    técnico = Column("Técnico", String(50))
    estado = Column("Estado", String(2))
    cidade = Column("Cidade", String(50))
    região = Column("Região", String(40))
    endereço = Column("Endereço", String(70))
    complemento = Column("Complemento", String(150))
    bairro = Column("Bairro", String(50))
    cep = Column("CEP", String(10))
    número = Column("número", String(50))
    id_do_equipamento = Column("ID do Equipamento", String(20))
    tipo_do_equipamento = Column("Tipo do Equipamento", String(20))
    observações_atendimento = Column("Observações Atendimento", String(20))
    observações = Column("Observações", Text)
    descrição_motivo = Column("Descrição Motivo", Text)
    descrição_motivo_1ª_visita = Column("Descrição Motivo 1ª Visita", Text)
    descrição_motivo_2ª_visita = Column("Descrição Motivo 2ª Visita", Text)
    defeito = Column("Defeito", String(40))
    solução = Column("Solução", String(20))
    remarks = Column("Remarks", Text)
    tipo_pessoa = Column("Tipo Pessoa", String(6))
    origem_da_venda = Column("Origem da Venda", String(50))
    vendedor = Column("Vendedor", String(50))
    criado_por = Column("Criado por:", String(50))
    última_modificação = Column("Última Modificação", String(50))
    numero_de_visitas = Column("NUMERO DE VISITAS", Integer)
    data_primeira_visita = Column("DATA PRIMEIRA VISITA", String(20))
    data_segunda_visita = Column("DATA SEGUNDA VISITA", String(20))
    data_de_reabertura_1 = Column("Data de Reabertura 1", String(20))
    data_de_reabertura_2 = Column("Data de Reabertura 2", String(20))
    abono = Column("Abono", String(5))
    kit = Column("Kit", String(5))
    quantidade_de_kits = Column("Quantidade de Kits", Integer)
    aberta_por_integração = Column("Aberta por Integração", String(5))
    baixa_mobile = Column("Baixa Mobile", String(5))
    foto_assinatura = Column("Foto/Assinatura", String(5))
    classe = Column("Classe", String(20))
    nome_da_causa = Column("Nome da Causa", String(20))
    os_emergencial = Column("OS Emergencial", String(5))
    flag_emergencial_modificado_por = Column(
        "Flag Emergencial Modificado Por", String(5))
    os_the_flash = Column("OS The Flash", String(5))
    flag_the_flash_modificado_por = Column(
        "Flag The Flash Modificado Por", String(5))
    data_abertura = Column("Data Abertura", DateTime)
    data_limite_cliente = Column("Data Limite Cliente", DateTime)
    data_limite = Column("Data Limite", DateTime)
    data_modificação = Column("Data Modificação", DateTime)
    data_atendimento = Column("Data Atendimento", DateTime)
    data_de_modificação_da_flag_emergencial = Column(
        "Data de Modificação da Flag Emergencial", DateTime)
    data_de_modificação_da_flag_the_flash = Column(
        "Data de Modificação da Flag The Flash", DateTime)
    status_atual = Column("Status_Atual", String(50))
    codtitulo_atualizado_stone = Column(
        "CodTitulo_Atualizado_Stone", String(50))
    data_retorno_stone = Column("Data_Retorno_Stone", DateTime)
    antigo_status = Column("ANTIGO_STATUS", String(20))
    dt_importado = Column("DT_IMPORTADO", DateTime)
