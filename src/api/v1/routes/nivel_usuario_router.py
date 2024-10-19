from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.database import get_session
from src.models.nivel_usuario_model import NivelUsuarioModel
from src.schemas.nivel_usuario_schema import NivelUsuarioSchema

router = APIRouter()


@router.get(path='/',
            description='Endpoint para recuperar todos os registros',
            summary=' ',
            response_model=List[NivelUsuarioSchema])
async def get_tipo_solicitacao(session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(NivelUsuarioModel)
        result = await db.execute(query)
        niveis_usuarios: List[NivelUsuarioModel] = result.scalars().all()
        return niveis_usuarios


@router.get(path='/{id}',
            description='Endpoint para recuperar registro pelo ID',
            summary=' ',
            response_model=NivelUsuarioSchema)
async def get_tipo_solicitacao_by_id(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(NivelUsuarioModel).filter(
            NivelUsuarioModel.id == id)
        result = await db.execute(query)
        nivel_usuario: List[NivelUsuarioModel] = result.scalar_one_or_none(
        )

        if nivel_usuario == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Nível de Usuário não encontrado.')

        return nivel_usuario


@router.post(path='/',
             description='Endpoint para salvar novo registro',
             summary=' ',
             status_code=status.HTTP_201_CREATED,
             response_model=NivelUsuarioSchema)
async def post_tipo_solicitacao(nivelUsuario: NivelUsuarioSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        nivel_usuario_novo: NivelUsuarioModel = NivelUsuarioModel()
        nivel_usuario_novo.nome = nivelUsuario.nome
        db.add(nivel_usuario_novo)
        await db.commit()
        return nivel_usuario_novo


@router.put(path='/{id}',
            description='Endpoint para atualizar registro pelo ID',
            summary=' ',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=NivelUsuarioSchema)
async def put_tipo_solicitacao(id: int, nivelUsuario: NivelUsuarioSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(NivelUsuarioModel).filter(
            NivelUsuarioModel.id == id)
        result = await db.execute(query)
        nivel_usuario_update = result.scalar_one_or_none()

        if nivel_usuario_update == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Nível de Usuário não encontrado.')
        else:
            nivel_usuario_update.nome = nivelUsuario.nome
            await db.commit()
            return nivel_usuario_update


@router.delete(path='/{id}',
               description='Endpoint para excluir registro pelo ID',
               summary=' ',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_tipo_solicitacao(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(NivelUsuarioModel).filter(
            NivelUsuarioModel.id == id)
        result = await db.execute(query)
        nivel_usuario_delete = result.scalar_one_or_none()

        if nivel_usuario_delete == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Tipo de solicitação não encontrado.')
        else:
            await db.delete(nivel_usuario_delete)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)