from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.auth import get_current_user
from src.core.database import get_session
from src.models import TipoIntegracaoModel, UsuarioModel
from src.schemas import TipoIntegracaoSchema

router = APIRouter()


@router.get(path='/',
            description='Endpoint para recuperar todos os registros',
            summary=' ',
            response_model=List[TipoIntegracaoSchema])
async def get_tipos_integracao(session: AsyncSession = Depends(get_session),
                               usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        query = select(TipoIntegracaoModel)
        result = await db.execute(query)
        tipos_integracao: List[TipoIntegracaoModel] = result.scalars().all()
        return tipos_integracao


@router.get(path='/{id}',
            description='Endpoint para recuperar registro pelo ID',
            summary=' ',
            response_model=TipoIntegracaoSchema)
async def get_tipo_integracao_by_id(id: int, session: AsyncSession = Depends(get_session),
                                    usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        query = select(TipoIntegracaoModel).filter(
            TipoIntegracaoModel.id == id)
        result = await db.execute(query)
        tipo_integracao: List[TipoIntegracaoModel] = result.scalar_one_or_none(
        )

        if tipo_integracao == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de Integração não encontrado.')

        return tipo_integracao


@router.post(path='/',
             description='Endpoint para salvar novo registro',
             summary=' ',
             status_code=status.HTTP_201_CREATED,
             response_model=TipoIntegracaoSchema)
async def post_tipo_integracao(tipo_integracao: TipoIntegracaoSchema,
                               session: AsyncSession = Depends(get_session),
                               usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        tipo_integracao_insert: TipoIntegracaoModel = TipoIntegracaoModel()
        tipo_integracao_insert.nome = tipo_integracao.nome
        tipo_integracao_insert.logo = tipo_integracao.logo
        db.add(tipo_integracao_insert)
        await db.commit()
        return tipo_integracao_insert


@router.put(path='/{id}',
            description='Endpoint para atualizar registro pelo ID',
            summary=' ',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=TipoIntegracaoSchema)
async def put_tipo_integracao(id: int, tipo_integracao: TipoIntegracaoSchema,
                              session: AsyncSession = Depends(get_session),
                              usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        query = select(TipoIntegracaoModel).filter(
            TipoIntegracaoModel.id == id)
        result = await db.execute(query)
        tipo_integracao_update = result.scalar_one_or_none()

        if tipo_integracao_update == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de Integração não encontrado.')
        else:
            tipo_integracao_update.nome = tipo_integracao.nome
            tipo_integracao_update.logo = tipo_integracao.logo
            await db.commit()
            return tipo_integracao_update


@router.delete(path='/{id}',
               description='Endpoint para excluir registro pelo ID',
               summary=' ',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_tipo_integracao(id: int, session: AsyncSession = Depends(get_session),
                                 usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with session as db:
        query = select(TipoIntegracaoModel).filter(
            TipoIntegracaoModel.id == id)
        result = await db.execute(query)
        tipo_integracao_delete = result.scalar_one_or_none()

        if tipo_integracao_delete == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de Integração não encontrado.')
        else:
            await db.delete(tipo_integracao_delete)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
