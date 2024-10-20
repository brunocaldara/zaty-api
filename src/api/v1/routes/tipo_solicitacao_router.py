from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.database import get_session
from src.models.tipo_solicitacao_model import TipoSolicitacaoModel
from src.schemas.tipo_solicitacao_schema import TipoSolicitacaoSchema

router = APIRouter()


@router.get(path='/',
            description='Endpoint para recuperar todos os registros',
            summary=' ',
            response_model=List[TipoSolicitacaoSchema])
async def get_tipos_solicitacao(session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoSolicitacaoModel)
        result = await db.execute(query)
        tipos_solicitacao: List[TipoSolicitacaoModel] = result.scalars().all()
        return tipos_solicitacao


@router.get(path='/{id}',
            description='Endpoint para recuperar registro pelo ID',
            summary=' ',
            response_model=TipoSolicitacaoSchema)
async def get_tipo_solicitacao_by_id(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoSolicitacaoModel).filter(
            TipoSolicitacaoModel.id == id)
        result = await db.execute(query)
        tipo_solicitacao: List[TipoSolicitacaoModel] = result.scalar_one_or_none(
        )

        if tipo_solicitacao == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de Solicitação não encontrado.')

        return tipo_solicitacao


@router.post(path='/',
             description='Endpoint para salvar novo registro',
             summary=' ',
             status_code=status.HTTP_201_CREATED,
             response_model=TipoSolicitacaoSchema)
async def post_tipo_solicitacao(tipo_solicitacao: TipoSolicitacaoSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        tipo_solicitacao_insert: TipoSolicitacaoModel = TipoSolicitacaoModel()
        tipo_solicitacao_insert.nome = tipo_solicitacao.nome
        db.add(tipo_solicitacao_insert)
        await db.commit()
        return tipo_solicitacao_insert


@router.put(path='/{id}',
            description='Endpoint para atualizar registro pelo ID',
            summary=' ',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=TipoSolicitacaoSchema)
async def put_tipo_solicitacao(id: int, tipo_solicitacao: TipoSolicitacaoSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoSolicitacaoModel).filter(
            TipoSolicitacaoModel.id == id)
        result = await db.execute(query)
        tipo_solicitacao_update = result.scalar_one_or_none()

        if tipo_solicitacao_update == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de Solicitação não encontrado.')
        else:
            tipo_solicitacao_update.nome = tipo_solicitacao.nome
            await db.commit()
            return tipo_solicitacao_update


@router.delete(path='/{id}',
               description='Endpoint para excluir registro pelo ID',
               summary=' ',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_tipo_solicitacao(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoSolicitacaoModel).filter(
            TipoSolicitacaoModel.id == id)
        result = await db.execute(query)
        tipo_solicitacao_delete = result.scalar_one_or_none()

        if tipo_solicitacao_delete == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de Solicitação não encontrado.')
        else:
            await db.delete(tipo_solicitacao_delete)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
