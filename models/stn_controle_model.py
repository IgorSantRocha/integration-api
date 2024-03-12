from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.stn_base_model import StnBaseModel
from sqlalchemy.sql import func


class StnControleModel(Base):
    __tablename__ = 'TB_STN_Integration'
    id = Column("ID", Integer, primary_key=True)
    chamado_id = Column("CHAMADO_ID", Integer, ForeignKey('TB_Stone.ID'))
    criadoem = Column(DateTime, default=func.now())
    status_desejado = Column("STATUS_DESEJADO", String(20))
    enviado = Column("ENVIADO", Boolean, default=0)
    atualizadoem = Column("ATUALIZADOEM", DateTime, default=func.now())
    msg_resposta = Column("MSG_RESPOSTA", String(30), nullable=True)
    statuscode_resposta = Column("STATUSCODE_RESPOSTA", Integer, nullable=True)
    # Definindo o relacionamento com StnBaseModel
    base = relationship(StnBaseModel, foreign_keys=[chamado_id])
