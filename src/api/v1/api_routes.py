from fastapi import APIRouter

from src.api.v1.routes import tipo_solicitacao_router

router = APIRouter()
router.include_router(tipo_solicitacao_router.router,
                      prefix='/tiposolicitacao', tags=['Tipo Solicitação'])
