from fastapi import APIRouter

from api.api_v1.endpoints import cars
from api.api_v1.endpoints import stn

api_router = APIRouter()
api_router.include_router(cars.router, prefix="/cars", tags=["cars"])
api_router.include_router(stn.router, prefix="/stn", tags=["Stone"])
