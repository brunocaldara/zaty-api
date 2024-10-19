from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.database import get_session
from src.models.tipo_solicitacao_model import TipoSolicitacaoModel
from src.schemas.tipo_solicitacao_schema import TipoSolicitacaoSchema

router = APIRouter()


@router.get(path='/',
            description='',
            summary='',
            response_model=List[TipoSolicitacaoSchema])
async def get_tipo_solicitacao(session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoSolicitacaoModel)
        result = await db.execute(query)
        tiposIntegracao: List[TipoSolicitacaoModel] = result.scalars().all()
        return tiposIntegracao


@router.get(path='/{id}',
            description='',
            summary='',
            response_model=TipoSolicitacaoSchema)
async def get_tipo_solicitacao_by_id(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoSolicitacaoModel).filter(
            TipoSolicitacaoModel.id == id)
        result = await db.execute(query)
        tipoIntegracao: List[TipoSolicitacaoModel] = result.scalar_one_or_none()

        if tipoIntegracao == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de solicitação não encontrado.')

        return tipoIntegracao


@router.post(path='/',
             description='',
             summary='',
             status_code=status.HTTP_201_CREATED,
             response_model=TipoSolicitacaoSchema)
async def post_tipo_solicitacao(tipoSolicitacao: TipoSolicitacaoSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        tipoSolicitacaoNovo: TipoSolicitacaoModel = TipoSolicitacaoModel()
        tipoSolicitacaoNovo.nome = tipoSolicitacao.nome
        db.add(tipoSolicitacaoNovo)
        await db.commit()
        return tipoSolicitacaoNovo


@router.put(path='/{id}',
            description='',
            summary='',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=TipoSolicitacaoSchema)
async def put_tipo_solicitacao(id: int, tipoSolicitacao: TipoSolicitacaoSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoSolicitacaoModel).filter(
            TipoSolicitacaoModel.id == id)
        result = await db.execute(query)
        tipoSolicitacaoUpdate = result.scalar_one_or_none()

        if tipoSolicitacaoUpdate == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de solicitação não encontrado.')
        else:
            tipoSolicitacaoUpdate.nome = tipoSolicitacao.nome
            await db.commit()
            return tipoSolicitacaoUpdate


@router.delete(path='/{id}',
               description='',
               summary='',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_tipo_solicitacao(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoSolicitacaoModel).filter(
            TipoSolicitacaoModel.id == id)
        result = await db.execute(query)
        tipoSolicitacaoDelete = result.scalar_one_or_none()

        if tipoSolicitacaoDelete == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de solicitação não encontrado.')
        else:
            await db.delete(tipoSolicitacaoDelete)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
