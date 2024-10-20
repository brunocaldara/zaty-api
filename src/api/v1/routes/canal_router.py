from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.database import get_session
from src.models.canal_model import CanalModel
from src.schemas.canal_schema import CanalSchema

router = APIRouter()


@router.get(path='/',
            description='Endpoint para recuperar todos os registros',
            summary=' ',
            response_model=List[CanalSchema])
async def get_tipo_solicitacao(session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(CanalModel)
        result = await db.execute(query)
        canais: List[CanalModel] = result.scalars().all()
        return canais


@router.get(path='/{id}',
            description='Endpoint para recuperar registro pelo ID',
            summary=' ',
            response_model=CanalSchema)
async def get_tipo_solicitacao_by_id(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(CanalModel).filter(CanalModel.id == id)
        result = await db.execute(query)
        canal: List[CanalModel] = result.scalar_one_or_none(
        )

        if canal == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Canal não encontrado.')

        return canal


@router.post(path='/',
             description='Endpoint para salvar novo registro',
             summary=' ',
             status_code=status.HTTP_201_CREATED,
             response_model=CanalSchema)
async def post_tipo_solicitacao(canal: CanalSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        canal_insert: CanalModel = CanalModel()
        canal_insert.nome = canal.nome
        db.add(canal_insert)
        await db.commit()
        return canal_insert


@router.put(path='/{id}',
            description='Endpoint para atualizar registro pelo ID',
            summary=' ',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=CanalSchema)
async def put_tipo_solicitacao(id: int, canal: CanalSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(CanalModel).filter(CanalModel.id == id)
        result = await db.execute(query)
        canal_update = result.scalar_one_or_none()

        if canal_update == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Canal não encontrado.')
        else:
            canal_update.nome = canal.nome
            await db.commit()
            return canal_update


@router.delete(path='/{id}',
               description='Endpoint para excluir registro pelo ID',
               summary=' ',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_tipo_solicitacao(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(CanalModel).filter(CanalModel.id == id)
        result = await db.execute(query)
        canal_delete = result.scalar_one_or_none()

        if canal_delete == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Canal não encontrado.')
        else:
            await db.delete(canal_delete)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
