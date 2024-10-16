from typing import List

from fastapi import APIRouter, status

from core.settings import settings
from models.tipo_solicitacao_model import TipoSolicitacaoModel
from schemas.tipo_solicitacao_schema import TipoSolicitacaoSchema

router = APIRouter(prefix=settings.API_URL_VERISON)

main_path = '/tipointegracao'


@router.get(path=f'{main_path}',
            description='',
            summary='',
            response_model=List[TipoSolicitacaoSchema])
async def get_tipo_integracao():
    return {'msg': 'teste'}


@router.post(main_path,
             description='',
             summary='',
             status_code=status.HTTP_201_CREATED,
             response_model=TipoSolicitacaoSchema)
async def post_tipo_integracao(tipoSolicitacao: TipoSolicitacaoSchema):
    pass
