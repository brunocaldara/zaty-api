from fastapi import APIRouter

from src.api.v1.routes import (atendimento_router, canal_router,
                               empresa_router, nivel_usuario_router,
                               tipo_integracao_router, tipo_solicitacao_router,
                               usuario_router)

router = APIRouter()

router.include_router(atendimento_router.router,
                      prefix='/atendimento', tags=['Atendimento'])
router.include_router(canal_router.router, prefix='/canal',
                      tags=['Canal'])
router.include_router(empresa_router.router,
                      prefix='/empresa', tags=['Empresa'])
router.include_router(nivel_usuario_router.router,
                      prefix='/nivelusuario', tags=['Nível Usuário'])
router.include_router(tipo_integracao_router.router,
                      prefix='/tipointegracao', tags=['Tipo Integração'])
router.include_router(tipo_solicitacao_router.router,
                      prefix='/tiposolicitacao', tags=['Tipo Solicitação'])
router.include_router(usuario_router.router,
                      prefix='/usuario', tags=['Usuário'])
