from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.database import get_session
from src.models.empresa_model import EmpresaModel
from src.models.usuario_model import UsuarioModel
from src.schemas.empresa_schema import EmpresaSchema

router = APIRouter()


@router.get(path='/',
            description='Endpoint para recuperar todos os registros',
            summary=' ',
            response_model=List[EmpresaSchema])
async def get_tipo_solicitacao(session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(EmpresaModel)
        result = await db.execute(query)
        empresas: List[EmpresaModel] = result.scalars().all()
        return empresas


@router.get(path='/{id}',
            description='Endpoint para recuperar registro pelo ID',
            summary=' ',
            response_model=EmpresaSchema)
async def get_tipo_solicitacao_by_id(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(EmpresaModel).filter(EmpresaModel.id == id)
        result = await db.execute(query)
        empresa: List[EmpresaModel] = result.scalar_one_or_none()

        if empresa == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Empresa não encontrada.')

        return empresa


@router.post(path='/',
             description='Endpoint para salvar novo registro',
             summary=' ',
             status_code=status.HTTP_201_CREATED,
             response_model=EmpresaSchema)
async def post_tipo_solicitacao(empresa: EmpresaSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        if empresa.usuario_id != None:
            query_usuario = select(UsuarioModel).filter(
                UsuarioModel.id == empresa.usuario_id)
            usuario_result = await db.execute(query_usuario)
            usuario = usuario_result.scalar_one_or_none()

            if usuario == None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail='Usuário inválido.')

        empresa_nova: EmpresaModel = EmpresaModel()
        empresa_nova.nome = empresa.nome
        empresa_nova.cnpj = empresa.cnpj
        empresa_nova.logo = empresa.logo
        empresa_nova.url_evo = empresa.url_evo
        empresa_nova.usuario_id = empresa.usuario_id
        empresa_nova.status = empresa.status
        empresa_nova.codigo_publico = empresa.codigo_publico
        db.add(empresa_nova)
        await db.commit()
        return empresa_nova


@router.put(path='/{id}',
            description='Endpoint para atualizar registro pelo ID',
            summary=' ',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=EmpresaSchema)
async def put_tipo_solicitacao(id: int, empresa: EmpresaSchema, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(EmpresaModel).filter(EmpresaModel.id == id)
        result = await db.execute(query)
        empresa_update = result.scalar_one_or_none()

        if empresa_update == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Empresa não encontrada.')
        else:
            empresa_update.nome = empresa.nome
            empresa_update.cnpj = empresa.cnpj
            empresa_update.logo = empresa.logo
            empresa_update.url_evo = empresa.url_evo
            empresa_update.usuario_id = empresa.usuario_id
            empresa_update.status = empresa.status
            empresa_update.codigo_publico = empresa.codigo_publico
        await db.commit()
        return empresa_update


@router.delete(path='/{id}',
               description='Endpoint para excluir registro pelo ID',
               summary=' ',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_tipo_solicitacao(id: int, session: AsyncSession = Depends(get_session)):
    async with session as db:
        query = select(EmpresaModel).filter(EmpresaModel.id == id)
        result = await db.execute(query)
        empresa_delete = result.scalar_one_or_none()

        if empresa_delete == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Empresa não encontrada.')
        else:
            await db.delete(empresa_delete)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
