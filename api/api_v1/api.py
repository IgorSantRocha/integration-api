from fastapi import APIRouter

from api.api_v1.endpoints.stn import stn_interno, stn_requests

api_router = APIRouter()
api_router.include_router(
    stn_interno.router, prefix="/stn", tags=["Stone - Controle interno"])
api_router.include_router(
    stn_requests.router, prefix="/stn", tags=["Stone - Requests"])
