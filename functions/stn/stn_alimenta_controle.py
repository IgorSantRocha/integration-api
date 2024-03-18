from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from crud.crud_stn import stn_controle, stn_base_essential
from models.stn_base_model import StnBaseEssentialModel
from schemas.stn_base_schema import StnBaseInDbBaseSC
from schemas.stn_controle_schema import StnControleCreateSC
from sqlalchemy.orm import Session
'''
Essa função tem como objetivo consultar a tabela da Stone
E alimentar a tabela de controle com os chamados a serem enviados na APIStone
'''


def cria_instancia_banco():
    engine = create_engine(
        str(settings.SQLALCHEMY_DATABASE_URI), pool_pre_ping=True)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session: Session = SessionLocal()
    # values = session.query(StnBaseEssentialModel).first()

    return session


def stn_consulta_base():
    session = cria_instancia_banco()

    casos_novos: list[StnBaseInDbBaseSC] = stn_base_essential.get_multi(  # type: ignore
        db=session, limit=2)
    # casos_novos: dict = stn_base_essential.get_multi_filter(
    #   db=session, filterby='status', filter='NOVA')
    stn_insere_chamados_no_controle(session, casos_novos)
    return casos_novos


def stn_insere_chamados_no_controle(db: Session, casos_novos: list[StnBaseEssentialModel]):
    # monto a lista de dicionários a ser inserida
    lista_chamados = []
    for caso in casos_novos:
        print(f"ID: {caso.id}, Status: {caso.status}")

        lista_chamados.append(StnControleCreateSC(
            status_desejado='EM CAMPO',
            chamado_id=caso.id
        ))
    print(lista_chamados)
    stn_controle.create_multi(db=db, obj_in=lista_chamados)

    return casos_novos


def stn_envia_requisicoes():
    pass


if __name__ == '__main__':
    casos_novos = stn_consulta_base()
    print(casos_novos)