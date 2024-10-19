from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.database import get_session
from src.models.tipo_integracao_model import TipoIntegracaoModel
from src.schemas.tipo_integracao_schema import TipoIntegracaoSchema

router = APIRouter()


@router.get(path='/',
            description='Endpoint para recuperar todos os registros',
            summary=' ',
            response_model=List[TipoIntegracaoSchema])
async def get_tipo_integracao(session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoIntegracaoModel)
        result = await db.execute(query)
        tiposIntegracao: List[TipoIntegracaoModel] = result.scalars().all()
        return tiposIntegracao


@router.get(path='/{id}',
            description='Endpoint para recuperar registro pelo ID',
            summary=' ',
            response_model=TipoIntegracaoSchema)
async def get_tipo_integracao_by_id(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoIntegracaoModel).filter(
            TipoIntegracaoModel.id == id)
        result = await db.execute(query)
        tipoIntegracao: List[TipoIntegracaoModel] = result.scalar_one_or_none()

        if tipoIntegracao == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de integração não encontrado.')

        return tipoIntegracao


@router.post(path='/',
             description='Endpoint para salvar novo registro',
             summary=' ',
             status_code=status.HTTP_201_CREATED,
             response_model=TipoIntegracaoSchema)
async def post_tipo_integracao(tipoIntegracao: TipoIntegracaoSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        tipoIntegracaoNovo: TipoIntegracaoModel = TipoIntegracaoModel()
        tipoIntegracaoNovo.nome = tipoIntegracao.nome
        tipoIntegracaoNovo.logo = tipoIntegracao.logo
        db.add(tipoIntegracaoNovo)
        await db.commit()
        return tipoIntegracaoNovo


@router.put(path='/{id}',
            description='Endpoint para atualizar registro pelo ID',
            summary=' ',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=TipoIntegracaoSchema)
async def put_tipo_integracao(id: int, tipoIntegracao: TipoIntegracaoSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoIntegracaoModel).filter(
            TipoIntegracaoModel.id == id)
        result = await db.execute(query)
        tipoIntegracaoUpdate = result.scalar_one_or_none()

        if tipoIntegracaoUpdate == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de integração não encontrado.')
        else:
            tipoIntegracaoUpdate.nome = tipoIntegracao.nome
            tipoIntegracaoUpdate.logo = tipoIntegracao.logo
            await db.commit()
            return tipoIntegracaoUpdate


@router.delete(path='/{id}',
               description='Endpoint para excluir registro pelo ID',
               summary=' ',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_tipo_integracao(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(TipoIntegracaoModel).filter(
            TipoIntegracaoModel.id == id)
        result = await db.execute(query)
        tipoIntegracaoDelete = result.scalar_one_or_none()

        if tipoIntegracaoDelete == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de integração não encontrado.')
        else:
            await db.delete(tipoIntegracaoDelete)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
