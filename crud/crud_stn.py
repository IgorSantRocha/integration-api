from crud.base import CRUDBase
from models.stn_base_model import StnBaseModel
from models.stn_controle_model import StnControleModel
from schemas.stn_controle_schema import StnControleCreateSC, StnControleUpdateSC


class CRUDItem(CRUDBase[StnControleModel, StnControleCreateSC, StnControleUpdateSC]):
    pass


stn_controle = CRUDItem(StnControleModel)
