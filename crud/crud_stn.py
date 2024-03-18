from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.stn_base_model import StnBaseModel
from models.stn_controle_model import StnControleModel
from schemas.stn_controle_schema import StnControleCreateSC, StnControleUpdateSC, StnControleUpdateStatusDesejadoSC


class StnControleCRUDItem(CRUDBase[StnControleModel, StnControleCreateSC, StnControleUpdateSC]):
    def update_status_desejado(
        self,
        db: Session,
        *,
        db_obj: StnControleModel,
        obj_in: Union[StnControleUpdateStatusDesejadoSC, Dict[str, Any]]
    ) -> StnControleModel:
        print('Entrei no método')
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        obj_data = jsonable_encoder(db_obj)
        return obj_data


stn_controle = StnControleCRUDItem(StnControleModel)


class StnBaseCRUDItem(CRUDBase[StnBaseModel, StnControleCreateSC, StnControleUpdateSC]):
    pass


stn_base = StnBaseCRUDItem(StnControleModel)
